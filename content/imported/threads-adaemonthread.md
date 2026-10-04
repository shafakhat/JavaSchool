---
title: A daemon thread.
nav: A daemon thread.
description: 1. A thread must be marked as a daemon thread before it is started.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20090602112319/http://www.java2s.com:80/Code/Java/Threads/Adaemonthread.htm
---
A daemon thread.

```java title=Example.java
class MyDaemon implements Runnable {
  Thread thrd;
  MyDaemon() {
    thrd = new Thread(this);
    thrd.setDaemon(true);
    thrd.start();
  }
  public boolean isDaemon(){
    return thrd.isDaemon();
  }
  public void run() {
    try {
      while(true) {
        System.out.print(".");
        Thread.sleep(100);
      }
    }
    catch(Exception exc) {
      System.out.println("MyDaemon interrupted.");
    }
  }
}
public class Main {
  public static void main(String args[]) throws Exception{
    MyDaemon dt = new MyDaemon();
    if(dt.isDaemon())
      System.out.println("dt is a daemon thread.");
    Thread.sleep(10000);
    System.out.println("\nMain thread ending.");
  }
}
```

1.  A thread must be marked as a daemon thread before it is started.
---  ---
2.  An application exits when there are no non-daemon threads running.
3.  A live daemon thread does not prevent an application from exiting.
