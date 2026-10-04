---
title: Producer, consumer and Queue
nav: Producer, consumer and Queue
description: Imported from the java2s.com archive: Producer, consumer and Queue
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20101012061335/http://www.java2s.com:80/Tutorial/Java/0160__Thread/ProducerconsumerandQueue.htm
---
```java title=Example.java
import java.util.Vector;
class Producer extends Thread {
  Queue queue;
  Producer(Queue queue) {
    this.queue = queue;
  }
  public void run() {
    int i = 0;
    while(true) {
      queue.add(i++);
    }
  }
}
class Consumer extends Thread {
  String str;
  Queue queue;
  Consumer(String str, Queue queue) {
    this.str = str;
    this.queue = queue;
  }
  public void run() {
    while(true) {
      System.out.println(str + ": " + queue.remove());
    }
  }
}
class Queue {
  private final static int SIZE = 5;
  private Vector queue = new Vector();
  private int count = 0;
  synchronized void add(int i) {
    while(count == SIZE) {
      try {
        wait();
      }
      catch(InterruptedException ie) {
        ie.printStackTrace();
        System.exit(0);
      }
    }
    queue.addElement(new Integer(i));
    ++count;
    notifyAll();
  }
  synchronized int remove() {
    while(count == 0) {
      try {
        wait();
      }
      catch(InterruptedException ie) {
        ie.printStackTrace();
        System.exit(0);
      }
    }
    Integer iobj = (Integer)queue.firstElement();
    queue.removeElement(iobj);
    --count;
    notifyAll();
    return iobj.intValue();
  }
}
class ProducerConsumers {
  public static void main(String args[]) {
    Queue queue = new Queue();
    new Producer(queue).start();
    new Consumer("ConsumerA", queue).start();
    new Consumer("ConsumerB", queue).start();
    new Consumer("ConsumerC", queue).start();
  }
}
```
