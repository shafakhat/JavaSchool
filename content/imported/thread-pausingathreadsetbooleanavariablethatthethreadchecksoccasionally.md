---
title: Pausing a Thread
nav: Pausing a Thread
description: Imported from the java2s.com archive: Pausing a Thread
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20100309133253/http://www.java2s.com:80/Tutorial/Java/0160__Thread/PausingaThreadsetbooleanavariablethatthethreadchecksoccasionally.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    MyThread thread = new MyThread();
    thread.start();
    while (true) {
      synchronized (thread) {
        thread.pause = true;
      }
      synchronized (thread) {
        thread.pause = false;
        thread.notify();
      }
    }
  }
}
class MyThread extends Thread {
  boolean pause = false;
  public void run() {
    while (true) {
      synchronized (this) {
        while (pause) {
          try {
            wait();
          } catch (Exception e) {
          }
        }
      }
    }
  }
}
```
