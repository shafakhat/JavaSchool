---
title: An example of CountDownLatch.
nav: An example of CountDownLat...
description: Imported from the java2s.com archive: An example of CountDownLatch.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20100209095856/http://java2s.com/Code/Java/Threads/AnexampleofCountDownLatch.htm
---
An example of CountDownLatch.

```java title=Example.java
import java.util.concurrent.CountDownLatch;
public class CDLDemo {
  public static void main(String args[]) {
    CountDownLatch cdl = new CountDownLatch(5);
    new MyThread(cdl);
    try {
      cdl.await();
    } catch (InterruptedException exc) {
      System.out.println(exc);
    }
    System.out.println("Done");
  }
}
class MyThread implements Runnable {
  CountDownLatch latch;
  MyThread(CountDownLatch c) {
    latch = c;
    new Thread(this).start();
  }
  public void run() {
    for(int i = 0; i<5; i++) {
      System.out.println(i);
      latch.countDown(); // decrement count
    }
  }
}
```

1.  Count Up Down Latch
