---
title: Another way to stop a thread
nav: Another way to stop a thread
description: public class AlternateStop extends Object implements Runnable {
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20070503201238/http://www.java2s.com:80/Code/Java/Threads/Anotherwaytostopathread.htm
---
```java title=Example.java
public class AlternateStop extends Object implements Runnable {
  private volatile boolean stopRequested;
  private Thread runThread;
  public void run() {
    runThread = Thread.currentThread();
    stopRequested = false;
    int count = 0;
    while (!stopRequested) {
      System.out.println("Running ... count=" + count);
      count++;
      try {
        Thread.sleep(300);
      } catch (InterruptedException x) {
         // re-assert interrupt
        Thread.currentThread().interrupt();
      }
    }
  }
  public void stopRequest() {
    stopRequested = true;
    if (runThread != null) {
      runThread.interrupt();
    }
  }
  public static void main(String[] args) {
    AlternateStop as = new AlternateStop();
    Thread t = new Thread(as);
    t.start();
    try {
      Thread.sleep(2000);
    } catch (InterruptedException x) {
    }
    as.stopRequest();
  }
}
```

Related examples in the same category
---
1. Is thread alive
2. Thread sleep
3. Another way to suspend and resume
4. Visual suspend and resume
5. Thread sleep and interrupt
6. Daemon Thread
