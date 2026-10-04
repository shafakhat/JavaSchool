---
title: A semaphore
nav: A semaphore
description: Thread thrdB = new Thread(new SyncOutput(sem, "Message 2!"));
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20091002222352/http://www.java2s.com:80/Code/Java/Threads/Asemaphore.htm
---
```java title=Example.java
import java.util.concurrent.Semaphore;
public class Main {
  public static void main(String args[]) throws Exception {
    Semaphore sem = new Semaphore(1, true);
    Thread thrdA = new Thread(new SyncOutput(sem, "Message 1"));
    Thread thrdB = new Thread(new SyncOutput(sem, "Message 2!"));
    thrdA.start();
    thrdB.start();
    thrdA.join();
    thrdB.join();
  }
}
class SyncOutput implements Runnable {
  Semaphore sem;
  String msg;
  SyncOutput(Semaphore s, String m) {
    sem = s;
    msg = m;
  }
  public void run() {
    try {
      sem.acquire();
      System.out.println(msg);
      Thread.sleep(10);
    } catch (Exception exc) {
      System.out.println("Error Writing File");
    }
    sem.release();
  }
}
```

1.  An implementation of a producer and consumer that use semaphores to control synchronization.
---  ---
2.  Semaphore that can allow a specified number of threads to enter, blocking the others.
3.  Wait exclusive semaphore with wait - notify primitives
