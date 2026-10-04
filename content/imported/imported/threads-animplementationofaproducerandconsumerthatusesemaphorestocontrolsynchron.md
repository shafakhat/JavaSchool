---
title: An implementation of a producer and consumer that use semaphores to control synchronization.
nav: An implementation of a pro...
description: An implementation of a producer and consumer that use semaphores to control synchronization. : Semaphore « Threads « Java
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20091002211221/http://www.java2s.com:80/Code/Java/Threads/Animplementationofaproducerandconsumerthatusesemaphorestocontrolsynchronization.htm
---
An implementation of a producer and consumer that use semaphores to control synchronization. : Semaphore « Threads « Java

```java title=Example.java
import java.util.concurrent.Semaphore;
class Queue {
  int value;
  static Semaphore semCon = new Semaphore(0);
  static Semaphore semProd = new Semaphore(1);
  void get() {
    try {
      semCon.acquire();
    } catch (InterruptedException e) {
      System.out.println("InterruptedException caught");
    }
    System.out.println("Got: " + value);
    semProd.release();
  }
  void put(int n) {
    try {
      semProd.acquire();
    } catch (InterruptedException e) {
      System.out.println("InterruptedException caught");
    }
    this.value = n;
    System.out.println("Put: " + n);
    semCon.release();
  }
}
class Producer implements Runnable {
  Queue q;
  Producer(Queue q) {
    this.q = q;
    new Thread(this, "Producer").start();
  }
  public void run() {
    for (int i = 0; i < 20; i++)
      q.put(i);
  }
}
class Consumer implements Runnable {
  Queue q;
  Consumer(Queue q) {
    this.q = q;
    new Thread(this, "Consumer").start();
  }
  public void run() {
    for (int i = 0; i < 20; i++)
      q.get();
  }
}
public class ProdCon {
  public static void main(String args[]) {
    Queue q = new Queue();
    new Consumer(q);
    new Producer(q);
  }
}
```

1.  A semaphore
---  ---
2.  Semaphore that can allow a specified number of threads to enter, blocking the others.
3.  Wait exclusive semaphore with wait - notify primitives
