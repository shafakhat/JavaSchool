---
title: Interrupt a thread.
nav: Interrupt a thread.
description: System.out.println(Thread.currentThread().getName() + " interrupted.");
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20100616084550/http://www.java2s.com:80/Tutorial/Java/0160__Thread/Interruptathread.htm
---
```java title=Example.java
class MyThread implements Runnable {
  public void run() {
    try {
      Thread.sleep(30000);
      for (int i = 1; i < 10; i++) {
        if (Thread.interrupted()) {
          System.out.println("interrupted.");
          break;
        }
      }
    } catch (Exception exc) {
      System.out.println(Thread.currentThread().getName() + " interrupted.");
    }
    System.out.println(Thread.currentThread().getName() + " exiting.");
  }
}
public class Main {
  public static void main(String args[]) throws Exception {
    Thread thrd = new Thread(new MyThread(), "MyThread #1");
    Thread thrd2 = new Thread(new MyThread(), "MyThread #2");
    thrd.start();
    Thread.sleep(100);
    thrd.interrupt();
    thrd2.start();
    Thread.sleep(400);
    thrd2.interrupt();
  }
}
```
