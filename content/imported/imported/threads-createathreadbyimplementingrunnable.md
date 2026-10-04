---
title: Create a thread by implementing Runnable.
nav: Create a thread by impleme...
description: Imported from the java2s.com archive: Create a thread by implementing Runnable.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20090622103303/http://www.java2s.com:80/Code/Java/Threads/CreateathreadbyimplementingRunnable.htm
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
      } while (count < 5);
    } catch (InterruptedException exc) {
      System.out.println("MyThread interrupted.");
    }
    System.out.println("MyThread terminating.");
  }
}
class RunnableDemo {
  public static void main(String args[]) {
    System.out.println("Main thread starting.");
    MyThread mt = new MyThread();
    Thread newThrd = new Thread(mt);
    newThrd.start();
    do {
      System.out.println("In main thread.");
      try {
        Thread.sleep(250);
      } catch (InterruptedException exc) {
        System.out.println("Main thread interrupted.");
      }
    } while (mt.count != 5);
    System.out.println("Main thread ending.");
  }
}
```

1.  Create a thread by extending Thread.
---  ---
2.  Thread Reminder
3.  Thread Race Demo
4.  Suggesting when to switch threads with yield()
5.  Creating threads with inner classes
6.  The safe way to stop a thread
7.  Calling sleep() to wait for a while
8.  Understanding join()
9.  Daemon threads spawn other daemon threads
10.  Daemon threads don't prevent the program from ending.
11.  Shows the use of thread priorities.
12.  Java new feature: threading
13.  Java 1.5 (5.0) new feature: Thread Schedule
14.  Two simple threads
15.  Simple threads creator
16.  Task
17.  SimpleThread using the Runnable interface.
18.  Very simple Threading example.
19.  Test Override Thread
20.  Test Override
21.  Parallelizing Loops for Multiprocessor Machines
22.  Listing All Running Threads in a group
23.  Setting priorities on the Thread objects
24.  Thread priorities.
25.  Use a ThreadGroup.
26.  Three Threads Test
