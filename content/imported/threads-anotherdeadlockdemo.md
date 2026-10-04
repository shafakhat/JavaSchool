---
title: Another deadlock demo : Java examples (example source code) » Threads » Deadlock
nav: Another deadlock demo : Ja...
description: Another deadlock demo : Java examples (example source code) » Threads » Deadlock
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20060513101518/http://www.java2s.com/Code/Java/Threads/Anotherdeadlockdemo.htm
---
Another deadlock demo : Java examples (example source code) » Threads » Deadlock

Another deadlock demo

```java title=Example.java
public class AnotherDeadLock {
  public static void main(String[] args) {
    final Object resource1 = "resource1";
    final Object resource2 = "resource2";
    // t1 tries to lock resource1 then resource2
    Thread t1 = new Thread() {
      public void run() {
        // Lock resource 1
        synchronized (resource1) {
          System.out.println("Thread 1: locked resource 1");
          try {
            Thread.sleep(50);
          } catch (InterruptedException e) {
          }
          synchronized (resource2) {
            System.out.println("Thread 1: locked resource 2");
          }
        }
      }
    };
    // t2 tries to lock resource2 then resource1
    Thread t2 = new Thread() {
      public void run() {
        synchronized (resource2) {
          System.out.println("Thread 2: locked resource 2");
          try {
            Thread.sleep(50);
          } catch (InterruptedException e) {
          }
          synchronized (resource1) {
            System.out.println("Thread 2: locked resource 1");
          }
        }
      }
    };
    // If all goes as planned, deadlock will occur,
    // and the program will never exit.
    t1.start();
    t2.start();
  }
}
```

Related examples in the same category
---
1. Demonstrates how deadlock can be hidden in a program
2. ReentrantLock: test for deadlocks
3. Deadlock Detecting
4. Using interrupt() to break out of a blocked thread.
