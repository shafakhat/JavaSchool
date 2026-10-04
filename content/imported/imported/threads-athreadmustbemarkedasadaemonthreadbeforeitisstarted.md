---
title: A thread must be marked as a daemon thread before it is started.
nav: A thread must be marked as...
description: A thread must be marked as a daemon thread before it is started.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20090602121723/http://www.java2s.com:80/Code/Java/Threads/Athreadmustbemarkedasadaemonthreadbeforeitisstarted.htm
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

1.  A daemon thread.
---  ---
2.  An application exits when there are no non-daemon threads running.
3.  A live daemon thread does not prevent an application from exiting.
