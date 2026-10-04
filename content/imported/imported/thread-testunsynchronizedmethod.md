---
title: Test Unsynchronized method
nav: Test Unsynchronized method
description: Imported from the java2s.com archive: Test Unsynchronized method
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20100616084239/http://www.java2s.com:80/Tutorial/Java/0160__Thread/TestUnsynchronizedmethod.htm
---
```java title=Example.java
public class TestUnsynchronized {
  int taskID;
  public void doAction(int val) {
    print("entering doAction()");
    taskID = val;
    print("doAction() taskID " + taskID);
    try {
      Thread.sleep(4000);
    } catch (InterruptedException x) {
    }
    print("doAction() sleep after taskID " + taskID);
    print("leaving performATask()");
  }
  public static void print(String msg) {
    String threadName = Thread.currentThread().getName();
    System.out.println(threadName + ": " + msg);
  }
  public static void main(String[] args) throws Exception {
    final TestUnsynchronized tus = new TestUnsynchronized();
    Runnable runA = new Runnable() {
      public void run() {
        tus.doAction(3);
      }
    };
    Thread ta = new Thread(runA, "threadA");
    ta.start();
    Thread.sleep(2000);
    Runnable runB = new Runnable() {
      public void run() {
        tus.doAction(7);
      }
    };
    Thread tb = new Thread(runB, "threadB");
    tb.start();
  }
}
```
