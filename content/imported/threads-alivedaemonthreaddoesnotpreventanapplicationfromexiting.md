---
title: A live daemon thread does not prevent an application from exiting.
nav: A live daemon thread does ...
description: A live daemon thread does not prevent an application from exiting.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20090602113711/http://www.java2s.com:80/Code/Java/Threads/Alivedaemonthreaddoesnotpreventanapplicationfromexiting.htm
---
```java title=Example.java
class MyThread extends Thread {
  MyThread() {
    setDaemon(true);
  }
  public void run() {
    boolean isDaemon = isDaemon();
    System.out.println("isDaemon:" + isDaemon);
  }
}
public class Main {
  public static void main(String[] argv) throws Exception {
    Thread thread = new MyThread();
    thread.setDaemon(true);
    thread.start();
  }
}
```

1.  A thread must be marked as a daemon thread before it is started.
---  ---
2.  A daemon thread.
3.  An application exits when there are no non-daemon threads running.
