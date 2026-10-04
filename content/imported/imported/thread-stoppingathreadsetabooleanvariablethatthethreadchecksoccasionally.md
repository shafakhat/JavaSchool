---
title: Stopping a Thread
nav: Stopping a Thread
description: Imported from the java2s.com archive: Stopping a Thread
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20100309133259/http://www.java2s.com:80/Tutorial/Java/0160__Thread/StoppingaThreadsetabooleanvariablethatthethreadchecksoccasionally.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    MyThread thread = new MyThread();
    thread.start();
    thread.stop = true;
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
