---
title: Daemon Thread
nav: Daemon Thread
description: Imported from the java2s.com archive: Daemon Thread
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20061104060934/http://www.java2s.com:80/Code/Java/Threads/DaemonThread.htm
---
```java title=Example.java
public class DaemonThread implements Runnable {
  public void run() {
    System.out.println("entering run()");
    try {
      System.out.println("in run(): currentThread() is"
          + Thread.currentThread());
      while (true) {
        try {
          Thread.sleep(500);
        } catch (InterruptedException x) {
        }
        System.out.println("in run(): woke up again");
      }
    } finally {
      System.out.println("leaving run()");
    }
  }
  public static void main(String[] args) {
    System.out.println("entering main()");
    Thread t = new Thread(new DaemonThread());
    t.setDaemon(true);
    t.start();
    try {
      Thread.sleep(3000);
    } catch (InterruptedException x) {
    }
    System.out.println("leaving main()");
  }
}
```

Related examples in the same category
---
1. Is thread alive
2. Thread sleep
3. Another way to stop a thread
4. Another way to suspend and resume
5. Visual suspend and resume
6. Thread sleep and interrupt
