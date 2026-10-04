---
title: A semaphore based coordination
nav: A semaphore based coordina...
description: Imported from the java2s.com archive: A semaphore based coordination
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20101118043233/http://www.java2s.com:80/Tutorial/Java/0160__Thread/Asemaphorebasedcoordination.htm
---
```java title=Example.java
import java.util.concurrent.Semaphore;
public class Main {
  public static void main(String args[]) throws Exception {
    Semaphore sem = new Semaphore(1, true);
    Thread thrdA = new Thread(new MyThread(sem, "Message 1"));
    Thread thrdB = new Thread(new MyThread(sem, "Message 2"));
    thrdA.start();
    thrdB.start();
    thrdA.join();
    thrdB.join();
  }
}
class MyThread implements Runnable {
  Semaphore sem;
  String msg;
  MyThread(Semaphore s, String m) {
    sem = s;
    msg = m;
  }
  public void run() {
    try {
      sem.acquire();
      System.out.println(msg);
      Thread.sleep(10);
      sem.release();
    } catch (Exception exc) {
      System.out.println("Error Writing File");
    }
  }
}
```
