---
title: Add a delay
nav: Add a delay
description: 8. Pausing the Current Thread: a thread can temporarily stop execution.
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20090717022406/http://www.java2s.com:80/Code/Java/Threads/Addadelay.htm
---
Add a delay

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    for (int i = 0; i < 10; i++) {
      System.out.println("i = " + i);
      try {
        Thread.sleep(1000);
      } catch (InterruptedException ie) {
        ie.printStackTrace();
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
15.  Determining When a Thread Has Finished
16.  Pause the execution of a thread using sleep()
