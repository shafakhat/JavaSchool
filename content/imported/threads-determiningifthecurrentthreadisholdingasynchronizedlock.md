---
title: Determining If the Current Thread Is Holding a Synchronized Lock
nav: Determining If the Current...
description: Determining If the Current Thread Is Holding a Synchronized Lock
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20090614055910/http://www.java2s.com:80/Code/Java/Threads/DeterminingIftheCurrentThreadIsHoldingaSynchronizedLock.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
  }
  public synchronized void myMethod() {
    Object o = new Object();
    System.out.println(Thread.holdsLock(o));
    synchronized (o) {
      System.out.println(Thread.holdsLock(o));
    }
    System.out.println(Thread.holdsLock(this));
  }
}
```

1.  Thread: Dining Philosophers
---  ---
2.  Synchronizing on another object
3.  Operations that may seem safe are not, when threads are present
4.  Synchronizing blocks instead of entire methods
5.  Boolean lock
6.  Static synchronized block
7.  Thread notify
8.  Thread deadlock
9.  Synchronize method
10.  Threads join
11.  Static synchronize
12.  No synchronize
13.  Thread syncronization
14.  Synchronized Block demo
15.  Interruptible Synchronized Block
16.  Signaling
17.  Simple Object FIFO
18.  Object FIFO
19.  Byte FIFO
20.  Thread Synch
21.  Daemon Lock
22.  Handle concurrent read/write: use synchronized to lock the data
23.  Lock for read and write
