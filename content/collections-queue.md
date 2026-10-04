---
title: Java Queue and Deque
nav: Queue & Deque (PriorityQueue, ArrayDeque)
description: Complete guide to Java queues and deques - Queue interface, PriorityQueue, ArrayDeque, LinkedList as queue, blocking queues and concurrency.
section: Collections
order: 70
---

## Queue family tree

```text title=hierarchy
Collection
├── Queue (FIFO base - offer/poll/peek)
│   ├── PriorityQueue / ArrayBlockingQueue (priority ordering)
│   ├── LinkedList (also a Deque - legacy use as queue)
│   ├── ArrayDeque (fastest array deque, can act as queue/stack)
│   ├── ConcurrentLinkedQueue (unbounded lock-free)
│   └── AbstractQueue helpers: ArrayBlockingQueue, DelayQueue,
│       PriorityBlockingQueue, SynchronousQueue, LinkedBlockingQueue...
└── SequencedCollection (Java 21) -> Deque (double-ended)
    ├── ArrayDeque          - ring buffer (default choice)
    ├── LinkedList          - node list (rarely right for queues)
    └── ConcurrentLinkedDeque / LinkedBlockingDeque
```

API ladder (how each method behaves):

| Situation | `add`/`remove` | `offer`/`poll`/`peek` | `element`/`last` |
|---|---|---|---|
| normal | works | works | works |
| queue empty (poll) | **throws** | returns **null** | — |
| queue full (offer) | **throws** | returns **false** | — |
| queue empty (element) | — | — | **throws** |
| deque ends | addFirst/addLast | offerFirst/offerLast, pollFirst/pollLast | getFirst/getLast (throw if empty) |

Rule: use **offer/poll/peek** for queues (non-throwing), **push/pop/peek** or **offerFirst/pollFirst** for deques.

## ArrayDeque - the default deque & stack

```java title=ArrayDequeDemo.java
import java.util.*;

public class ArrayDequeDemo {
    public static void main(String[] args) {
        Deque<String> dq = new ArrayDeque<>();     // ring buffer, no nulls

        // as a QUEUE (FIFO)
        dq.offer("first");
        dq.offer("second");
        System.out.println(dq.poll());             // first  (head)
        System.out.println(dq.peek());             // second

        // as a STACK (LIFO) - the modern replacement for Stack/Vector
        dq.push("on-top");                         // == addFirst
        System.out.println(dq.pop());              // on-top == removeFirst

        // as a DOUBLE-ENDED queue
        dq.offerLast("tail");
        dq.offerFirst("head");
        System.out.println(dq);                    // [head, second, tail]

        // iteration order: insertion order of the deque (from head)
        dq.forEach(System.out::println);
        System.out.println("contains: " + dq.contains("tail"));
    }
}
```

Why it wins: one array, circular reuse (no shifting), no node overhead, O(1) ends, null-free. Beats LinkedList for stacks/queues/breadth-first search/undo buffers.

## PriorityQueue (binary heap)

```java title=PriorityQueueDemo.java
import java.util.*;

public class PriorityQueueDemo {
    public static void main(String[] args) {
        // natural order
        Queue<Integer> pq = new PriorityQueue<>();
        pq.offer(5); pq.offer(1); pq.offer(9);
        System.out.println(pq.peek());             // 1 - head is smallest
        System.out.println(pq.poll());             // 1
        System.out.println(pq.poll());             // 5 (heap reorders internally)
        System.out.println(pq.poll());             // 9

        // custom comparator
        Queue<String> byLen = new PriorityQueue<>(Comparator.comparingInt(String::length));
        byLen.addAll(List.of("aaaa", "b", "cc"));
        System.out.println(byLen.poll());          // b

        // objects
        record Job(String name, int priority) {}
        Queue<Job> jobs = new PriorityQueue<>(Comparator.comparingInt(Job::priority));
        jobs.add(new Job("render", 3));
        jobs.add(new Job("sync", 1));
        System.out.println(jobs.poll().name());    // sync
    }
}
```

Trap: **iteration is NOT sorted** - only `poll()` sequence is. No nulls (NPE on offer(null)). Not thread-safe → `PriorityBlockingQueue` for concurrent.

## The blocking queues (producer → consumer backbone)

```java title=BlockingQueues.java
import java.util.concurrent.*;
import java.util.List;

public class BlockingQueues {
    public static void main(String[] args) throws Exception {
        // bounded array - backpressure when full
        BlockingQueue<String> work = new ArrayBlockingQueue<>(3);
        work.put("job1");                                  // waits if full
        String job = work.poll(1, TimeUnit.SECONDS);       // timed take

        // unbounded linked - optional capacity for throughput tuning
        BlockingQueue<String> logs = new LinkedBlockingQueue<>(1000);
        logs.offer("boot");

        // hand-off - no buffering, direct rendezvous (thread pools use it)
        BlockingQueue<String> pipe = new SynchronousQueue<>();
        new Thread(() -> {
            try { pipe.put("hi"); } catch (InterruptedException e) {}
        }).start();
        System.out.println(pipe.take());

        // take() blocks until an element arrives - the classic consumer loop
        new Thread(() -> {
            try {
                while (true) System.out.println("got " + work.take());
            } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        }).start();
        work.add("job2");
    }
}
```

Also: `DelayQueue` (elements usable after expiry - schedulers), `PriorityBlockingQueue` (priority under concurrency), `LinkedTransferQueue` (producer waits for consumer), `SynchronousQueue` (0-capacity hand-off).

## Concurrent queues

```java title=CLQ.java
import java.util.concurrent.ConcurrentLinkedQueue;

public class CLQ {
    public static void main(String[] args) {
        Queue<Integer> q = new ConcurrentLinkedQueue<>();   // unbounded, lock-free (CAS)
        q.offer(1); q.offer(2);
        System.out.println(q.poll());     // 1 - never blocks, null when empty
        // weakly consistent iteration: may reflect concurrent changes, never CME
        q.forEach(System.out::println);
    }
}
```

| Queue | Bounded? | Blocks? | Use |
|---|---|---|---|
| ConcurrentLinkedQueue | no | no | general concurrent FIFO |
| ArrayBlockingQueue | yes | offer/take block | simple producer-consumer |
| LinkedBlockingQueue | optional | yes | higher-throughput pool queues |
| SynchronousQueue | 0 | rendezvous | hand-off, cache-style executors |
| PriorityBlockingQueue | no | take blocks | scheduled/priority work |
| DelayQueue | no | take waits | timed release |

## Recipes

```java title=Recipes.java
import java.util.*;
import java.util.concurrent.*;

public class Recipes {
    public static void main(String[] args) throws Exception {
        // 1. BFS with a deque
        Deque<Integer> frontier = new ArrayDeque<>();
        frontier.offer(0);

        // 2. Undo stack
        Deque<String> undo = new ArrayDeque<>();
        undo.push("typing");
        String last = undo.pop();

        // 3. Sliding window "recent 3"
        Deque<String> recent = new ArrayDeque<>();
        for (String evt : List.of("a", "b", "c", "d")) {
            recent.offerLast(evt);
            if (recent.size() > 3) recent.pollFirst();
        }
        System.out.println(recent);                  // [b, c, d]

        // 4. Merge k sorted streams with a priority queue
        Queue<int[]> minHeap = new PriorityQueue<>((x, y) -> x[0] - y[0]);
        minHeap.offer(new int[]{1, 0});               // {value, streamId}
        minHeap.offer(new int[]{3, 1});
        int[] smallest = minHeap.poll();              // {1, 0}

        // 5. ThreadPoolExecutor's work queue in one line
        ExecutorService pool = Executors.newFixedThreadPool(2);
        BlockingQueue<Runnable> backing = new LinkedBlockingQueue<>(16);
        pool.shutdown();
    }
}
```

Related: [Collections overview](collections.html) · [List](collections-list.html) · [Set](collections-set.html) · [Map](collections-map.html) · [Producer-consumer in the archive](thread-producerconsumerandqueue.html)
