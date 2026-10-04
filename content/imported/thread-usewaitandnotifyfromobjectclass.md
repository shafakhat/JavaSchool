---
title: Use wait() and notify() from Object class
nav: Use wait() and notify() fr...
description: System.out.println(Thread.currentThread().getName()+ " is entering waitFor().");
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20100307182621/http://www.java2s.com:80/Tutorial/Java/0160__Thread/UsewaitandnotifyfromObjectclass.htm
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
