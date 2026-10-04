---
title: A queue(LinkedList) is used to coordinate work between a producer and a set of worker threads.
nav: A queue(LinkedList) is use...
description: public synchronized Object getWork() throws InterruptedException {
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20101012061330/http://www.java2s.com:80/Tutorial/Java/0160__Thread/AqueueLinkedListisusedtocoordinateworkbetweenaproducerandasetofworkerthreads.htm
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
