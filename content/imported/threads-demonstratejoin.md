---
title: Demonstrate join().
nav: Demonstrate join().
description: 6. Launch many programs using Thread and use join() to wait for the completion.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20100212074649/http://java2s.com/Code/Java/Threads/Demonstratejoin.htm
---
```java title=Example.java
class MyThread implements Runnable {
  int count;
  MyThread() {
    count = 0;
  }
  public void run() {
    System.out.println("MyThread starting.");
    try {
      do {
        Thread.sleep(500);
        System.out.println("In MyThread, count is " + count);
        count++;
      } while (count < 6);
    } catch (InterruptedException exc) {
      System.out.println("MyThread interrupted.");
    }
    System.out.println("MyThread terminating.");
  }
}
public class Main {
  public static void main(String args[]) {
    System.out.println("Main thread starting.");
    Thread thrd = new Thread(new MyThread());
    thrd.start();
    try {
      thrd.join();
    } catch (InterruptedException exc) {
      System.out.println("Main thread interrupted.");
    }
    System.out.println("Main thread ending.");
  }
}
```

1.  Wait the for the completion of a thread
---  ---
2.  Wait for the threads to finish
3.  A simple demonstration of wait() and notify().
4.  Suspend, resume, and stop a thread.
5.  Waiting on an object
6.  Launch many programs using Thread and use join() to wait for the completion.
