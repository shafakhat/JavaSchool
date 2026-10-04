---
title: Java Threads
nav: Threads
description: Create threads with Thread and Runnable, understand synchronization, races and the ExecutorService.
section: Core Java
order: 30
---

## What is a thread?

A **thread** is a unit of execution inside a process. Every Java program starts with at least one thread (`main`); the JVM adds others (GC, JIT...). More threads = overlapping work: one can wait on I/O while another computes.

```text title=One process, many threads
 Process (memory, heap shared)
 ├── thread: main
 ├── thread: worker-1
 └── thread: worker-2
```

## Creating threads - two ways

```java title=TwoWays.java
class MyThread extends Thread {          // way 1: extend Thread
    @Override
    public void run() {
        System.out.println("running in " + getName());
    }
}

public class TwoWays implements Runnable {  // way 2: implement Runnable (preferred)
    @Override
    public void run() {
        System.out.println("running in " + Thread.currentThread().getName());
    }

    public static void main(String[] args) throws InterruptedException {
        MyThread t1 = new MyThread();
        t1.start();                       // start() - NOT run() (run() would be a plain call)

        Thread t2 = new Thread(new TwoWays());
        t2.start();

        // lambda - the modern one-liner (Runnable is a functional interface)
        Thread t3 = new Thread(() -> System.out.println("lambda thread " + Thread.currentThread().getName()));
        t3.start();

        t1.join();                        // wait until t1 finishes
        t2.join();
        t3.join();
        System.out.println("all joined");
    }
}
```

> **Warning:** Calling `t.run()` executes the code *synchronously on the current thread*. Only `t.start()` creates a new thread. This is a classic bug.

Prefer `Runnable` (or `Callable`) over extending `Thread` - it separates *the work* from *the runner*, and leaves your class free to extend something else.

## Waiting for threads

| Method | Meaning |
|---|---|
| `t.join()` | current thread waits until `t` finishes |
| `t.sleep(ms)` | pause current thread (doesn't release locks) |
| `t.interrupt()` | request another thread to stop waiting/sleeping |
| `t.isAlive()` | is it still running? |

```java title=JoinDemo.java
public class JoinDemo {
    public static void main(String[] args) throws InterruptedException {
        Thread worker = new Thread(() -> {
            try {
                Thread.sleep(300);       // simulate work
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("worker done");
        });

        worker.start();
        worker.join();                   // main blocks here until worker finishes
        System.out.println("main continues after join");
    }
}
```

## The shared-state problem

Threads share the heap. Concurrent read-modify-write without protection produces **race conditions**:

```java title=Race.java
public class Race {
    static int counter = 0;

    public static void main(String[] args) throws InterruptedException {
        Runnable task = () -> {
            for (int i = 0; i < 10_000; i++) {
                counter++;               // NOT atomic: read -> add -> write
            }
        };

        Thread a = new Thread(task);
        Thread b = new Thread(task);
        a.start();
        b.start();
        a.join();
        b.join();

        System.out.println("counter = " + counter);   // 20000? 19871? varies!
    }
}
```

Two threads can read the same value, both add 1, and one increment is **lost**. The result is unpredictable - that's the race.

## `synchronized` - making it safe

```java title=Sync.java
public class Sync {
    private int counter = 0;
    private final Object lock = new Object();

    synchronized void increment() {           // locks 'this'
        counter++;
    }

    void incrementLocked() {
        synchronized (lock) {                 // locks a dedicated object
            counter++;
        }
    }

    synchronized int get() {                  // readers need the lock too
        return counter;
    }

    public static void main(String[] args) throws InterruptedException {
        Sync s = new Sync();
        Runnable task = () -> {
            for (int i = 0; i < 10_000; i++) s.increment();
        };

        Thread a = new Thread(task);
        Thread b = new Thread(task);
        a.start(); b.start();
        a.join(); b.join();

        System.out.println("counter = " + s.get());   // always 20000
    }
}
```

Rules of thumb:

- **Guard every shared mutable field** with the same lock.
- Keep `synchronized` blocks **short** - they serialize your program.
- Never lock on `this` publicly (callers can lock you out) - use a private lock object.

### Deadlock

```text title=The classic deadlock
 Thread 1: locks A, waits for B
 Thread 2: locks B, waits for A   <- nobody can move
```

Avoid it by always acquiring multiple locks **in the same global order**, or by not holding locks while doing slow work (I/O, network).

## Higher-level tools

For real applications, don't manage threads by hand. Use `ExecutorService`:

```java title=Executor.java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Executor {
    public static void main(String[] args) throws Exception {
        ExecutorService pool = Executors.newFixedThreadPool(3);

        Future<Integer> f = pool.submit(() -> {
            Thread.sleep(200);            // pretend this is heavy
            return 6 * 7;
        });

        for (int i = 1; i <= 5; i++) {
            final int jobId = i;
            pool.submit(() -> System.out.println("job " + jobId + " on " + Thread.currentThread().getName()));
        }

        System.out.println("result = " + f.get());   // waits for the future
        pool.shutdown();                             // no new tasks; let it drain
    }
}
```

Benefits: fixed pool size (no thread explosion), `Future` results, and clean shutdown.

## Thread safety options (pick the easiest that works)

1. **Don't share** - keep data local (no problem at all).
2. **Make it immutable** - `String`, records, `final` objects.
3. **Use a concurrent collection** - `ConcurrentHashMap`, `CopyOnWriteArrayList`, `AtomicInteger`.
4. **Synchronize** - explicit locks when you must.
5. **Confine** - one thread owns the data (actor style).

```java title=Atomic.java
import java.util.concurrent.atomic.AtomicInteger;

public class Atomic {
    static AtomicInteger safe = new AtomicInteger(0);

    public static void main(String[] args) throws InterruptedException {
        Runnable r = () -> { for (int i = 0; i < 10_000; i++) safe.incrementAndGet(); };
        Thread a = new Thread(r), b = new Thread(r);
        a.start(); b.start(); a.join(); b.join();
        System.out.println("atomic = " + safe.get());   // always 20000
    }
}
```

## Volatile

`volatile` guarantees visibility of writes across threads (no caching), but **not atomicity** of compound operations like `x++`:

```java title=Volatile.java
public class Volatile {
    static volatile boolean running = true;   // every thread sees the real value

    public static void main(String[] args) throws InterruptedException {
        Thread t = new Thread(() -> {
            int loops = 0;
            while (running) { loops++; }
            System.out.println("stopped after ~" + loops + " loops");
        });
        t.start();
        Thread.sleep(100);
        running = false;                      // cleanly stops the loop
        t.join();
    }
}
```

Next: [Lambdas](lambdas.html) - concise behavior as values.
