---
title: Determining If the Current Thread Is Holding a Synchronized Lock
nav: Determining If the Current...
description: Imported from the java2s.com archive: Determining If the Current Thread Is Holding a Synchronized Lock
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100616084215/http://www.java2s.com:80/Tutorial/Java/0160__Thread/DeterminingIftheCurrentThreadIsHoldingaSynchronizedLock.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    Object o = new Object();
    System.out.println(Thread.holdsLock(o));
    synchronized (o) {
      System.out.println(Thread.holdsLock(o));
    }
  }
}
```
