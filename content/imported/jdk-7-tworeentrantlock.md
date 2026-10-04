---
title: Two ReentrantLock
nav: Two ReentrantLock
description: Imported from the java2s.com archive: Two ReentrantLock
section: Imported - java2s Archive
order: 1129
source: https://web.archive.org/web/20130821064716/http://java2s.com/Code/Java/JDK-7/TwoReentrantLock.htm
---
```java title=Example.java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
public class Test {
  public static void main(String[] args) {
    final Lock firstLock = new ReentrantLock();
    final Lock secondLock = new ReentrantLock();
    firstLock.lock();
    Thread secondThread = new Thread(new Runnable() {
      public void run() {
        secondLock.lock();
        firstLock.lock();
      }
    });
    secondThread.start();
    try {
      Thread.sleep(250);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    secondLock.lock();
    secondLock.unlock();
    firstLock.unlock();
  }
}
```

1.  Use ReentrantLock
---  ---
2.  Use ReentrantLock to coordinate
3.  LinkedBlockingQueue and ThreadPoolExecutor
