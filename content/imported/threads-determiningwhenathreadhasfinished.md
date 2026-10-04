---
title: Determining When a Thread Has Finished
nav: Determining When a Thread ...
description: 8. Pausing the Current Thread: a thread can temporarily stop execution.
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20090720053121/http://www.java2s.com:80/Code/Java/Threads/DeterminingWhenaThreadHasFinished.htm
---
Determining When a Thread Has Finished

```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    Thread thread = new MyThread();
    thread.start();
    if (thread.isAlive()) {
      System.out.println("Thread has not finished");
    } else {
      System.out.println("Finished");
    }
    long delayMillis = 5000; // 5 seconds
    thread.join(delayMillis);
    if (thread.isAlive()) {
      System.out.println("thread has not finished");
    } else {
      System.out.println("Finished");
    }
    thread.join();
  }
}
class MyThread extends Thread {
  boolean stop = false;
  public void run() {
    while (true) {
      if (stop) {
        return;
      }
    }
  }
}
```

1.  Is thread alive
---  ---
2.  Thread sleep
3.  Another way to stop a thread
4.  Another way to suspend and resume
5.  Visual suspend and resume
6.  Thread sleep and interrupt
7.  Daemon Thread
8.  Pausing the Current Thread: a thread can temporarily stop execution.
9.  Pausing a Thread: set a variable that the thread checks occasionally, call Object.wait()
10.  set Uncaught Exception Handler
11.  Monitor a thread's status.
12.  Pause the execution
13.  Interrupt a thread.
14.  Stopping a Thread: set a variable that the thread checks occasionally
15.  Add a delay
16.  Pause the execution of a thread using sleep()
