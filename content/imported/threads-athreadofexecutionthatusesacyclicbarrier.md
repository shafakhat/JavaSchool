---
title: A thread of execution that uses a CyclicBarrier
nav: A thread of execution that...
description: Imported from the java2s.com archive: A thread of execution that uses a CyclicBarrier
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20090322135648/http://www.java2s.com:80/Code/Java/Threads/AthreadofexecutionthatusesaCyclicBarrier.htm
---
```java title=Example.java
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;
class BarDemo {
  public static void main(String args[]) {
    CyclicBarrier cb = new CyclicBarrier(3, new BarAction());
    System.out.println("Starting");
    new MyThread(cb, "A");
    new MyThread(cb, "B");
    new MyThread(cb, "C");
  }
}
class MyThread implements Runnable {
  CyclicBarrier cbar;
  String name;
  MyThread(CyclicBarrier c, String n) {
    cbar = c;
    name = n;
    new Thread(this).start();
  }
  public void run() {
    System.out.println(name);
    try {
      cbar.await();
    } catch (BrokenBarrierException exc) {
      System.out.println(exc);
    } catch (InterruptedException exc) {
      System.out.println(exc);
    }
  }
}
class BarAction implements Runnable {
  public void run() {
    System.out.println("Barrier Reached!");
  }
}
public class MainClass {
  public static void main(String args[]) {
    CyclicBarrier cb = new CyclicBarrier(3, new BarAction());
    System.out.println("Starting");
    new MyThread(cb, "A");
    new MyThread(cb, "B");
    new MyThread(cb, "C");
    new MyThread(cb, "X");
    new MyThread(cb, "Y");
    new MyThread(cb, "Z");
  }
}
```
