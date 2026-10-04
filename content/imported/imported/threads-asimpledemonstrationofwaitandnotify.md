---
title: A simple demonstration of wait() and notify().
nav: A simple demonstration of ...
description: System.out.println(Thread.currentThread().getName()+ " is entering waitFor().");
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20090810171618/http://www.java2s.com:80/Code/Java/Threads/Asimpledemonstrationofwaitandnotify.htm
---
```java title=Example.java
class MyResource {
  boolean ready = false;
  synchronized void waitFor() throws Exception {
    System.out.println(Thread.currentThread().getName()+ " is entering waitFor().");
      while (!ready)
        wait();
    System.out.println(Thread.currentThread().getName() + " resuming execution.");
  }
  synchronized void start() {
    ready = true;
    notify();
  }
}
class MyThread implements Runnable {
  MyResource myResource;
  MyThread(String name, MyResource so) {
    myResource = so;
    new Thread(this, name).start();
  }
  public void run() {
    try {
      myResource.waitFor();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
public class Main {
  public static void main(String args[]) throws Exception {
    MyResource sObj = new MyResource();
    new MyThread("MyThread", sObj);
    for (int i = 0; i < 10; i++) {
      Thread.sleep(50);
      System.out.print(".");
    }
    sObj.start();
  }
}
```

1.  Wait the for the completion of a thread
---  ---
2.  Wait for the threads to finish
3.  Demonstrate join().
4.  Suspend, resume, and stop a thread.
5.  Waiting on an object
6.  Launch many programs using Thread and use join() to wait for the completion.
