---
title: Creating a Bounded Work Queue
nav: Creating a Bounded Work Qu...
description: BlockingQueue<Integer> queue = new ArrayBlockingQueue<Integer>(capacity);
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20090831112931/http://www.java2s.com:80/Code/Java/Threads/CreatingaBoundedWorkQueue.htm
---
Creating a Bounded Work Queue

```java title=Example.java
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
public class Main {
  public static void main(String[] argv) throws Exception {
    int capacity = 10;
    BlockingQueue<Integer> queue = new ArrayBlockingQueue<Integer>(capacity);
    int numWorkers = 2;
    Worker[] workers = new Worker[numWorkers];
    for (int i = 0; i < workers.length; i++) {
      workers[i] = new Worker(queue);
      workers[i].start();
    }
    for (int i = 0; i < 100; i++) {
      queue.put(i);
    }
  }
}
class Worker extends Thread {
  BlockingQueue<Integer> q;
  Worker(BlockingQueue<Integer> q) {
    this.q = q;
  }
  public void run() {
    try {
      while (true) {
        Integer x = q.take();
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

1.  Implementing an Unbounded Work Queue
