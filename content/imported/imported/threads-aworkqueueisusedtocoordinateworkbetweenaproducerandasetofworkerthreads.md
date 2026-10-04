---
title: A work queue is used to coordinate work between a producer and a set of worker threads.
nav: A work queue is used to co...
description: A work queue is used to coordinate work between a producer and a set of worker threads.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20090615215854/http://www.java2s.com:80/Code/Java/Threads/Aworkqueueisusedtocoordinateworkbetweenaproducerandasetofworkerthreads.htm
---
```java title=Example.java
import java.util.LinkedList;
public class Main {
  public static void main(String[] argv) {
    WorkQueue queue = new WorkQueue();
    int numWorkers = 2;
    Worker[] workers = new Worker[numWorkers];
    for (int i = 0; i < workers.length; i++) {
      workers[i] = new Worker(queue);
      workers[i].start();
    }
    for (int i = 0; i < 100; i++) {
      queue.addWork(i);
    }
  }
}
class WorkQueue {
  LinkedList<Object> queue = new LinkedList<Object>();
  public synchronized void addWork(Object o) {
    queue.addLast(o);
    notify();
  }
  public synchronized Object getWork() throws InterruptedException {
    while (queue.isEmpty()) {
      wait();
    }
    return queue.removeFirst();
  }
}
class Worker extends Thread {
  WorkQueue q;
  Worker(WorkQueue q) {
    this.q = q;
  }
  public void run() {
    try {
      while (true) {
        Object x = q.getWork();
        if (x == null) {
          break;
        }
        System.out.println(x);
      }
    } catch (InterruptedException e) {
    }
  }
}
```

1.  Java 1.5 (5.0) new features: PriorityQueue
---  ---
2.  Safe list copy
3.  Safe vector copy
4.  Safe collection operation
5.  Java 1.5 (5.0) new feature: collection and thread
6.  Java Thread Performance: Collection Test
7.  Java Thread Performance: AtomicTest
8.  Rhyming Words
9.  Communicate between threads using a Queue
10.  Using a Thread-Local Variable
11.  Return a value from a thread.
