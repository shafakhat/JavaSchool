---
title: Waiting on an object
nav: Waiting on an object
description: Imported from the java2s.com archive: Waiting on an object
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20100616084554/http://www.java2s.com:80/Tutorial/Java/0160__Thread/Waitingonanobject.htm
---
```java title=Example.java
public class Main {
  public static void main(String str[]) {
    final Object monitor = new Object();
    new Thread() {
      public void run() {
        try {
          synchronized (monitor) {
            System.out.println("10 seconds ...");
            monitor.wait(10000);
            System.out.println("Wait over");
          }
        } catch (Throwable t) {
          t.printStackTrace();
        }
      }
    }.start();
  }
}
```
