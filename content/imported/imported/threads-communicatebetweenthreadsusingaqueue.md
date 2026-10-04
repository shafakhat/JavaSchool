---
title: Communicate between threads using a Queue
nav: Communicate between thread...
description: 10. A work queue is used to coordinate work between a producer and a set of worker threads.
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20090615220857/http://www.java2s.com:80/Code/Java/Threads/CommunicatebetweenthreadsusingaQueue.htm
---
```java title=Example.java
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
class PrepareProduction implements Runnable {
  BlockingQueue<String> queue;
  PrepareProduction(BlockingQueue<String> q) {
    queue = q;
  }
  public void run() {
    String thisLine;
    try {
      queue.put("1");
      queue.put("done");
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
class DoProduction implements Runnable {
  private final BlockingQueue<String> queue;
  DoProduction(BlockingQueue<String> q) {
    queue = q;
  }
  public void run() {
    try {
      String value = queue.take();
      while (!value.equals("done")) {
        value = queue.take();
        System.out.println(value);
      }
    } catch (Exception e) {
      System.out.println(Thread.currentThread().getName() + " "
          + e.getMessage());
    }
  }
}
public class Main {
  public static void main(String[] args) throws Exception {
    BlockingQueue<String> q = new LinkedBlockingQueue<String>();
    Thread p1 = new Thread(new PrepareProduction(q));
    Thread c1 = new Thread(new DoProduction(q));
    p1.start();
    c1.start();
    p1.join();
    c1.join();
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
9.  Using a Thread-Local Variable
10.  A work queue is used to coordinate work between a producer and a set of worker threads.
11.  Return a value from a thread.
