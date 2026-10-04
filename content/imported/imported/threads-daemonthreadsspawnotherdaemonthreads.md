---
title: Daemon threads spawn other daemon threads : Java examples (example source code) » Threads » Simple Threads
nav: Daemon threads spawn other...
description: Daemon threads spawn other daemon threads : Java examples (example source code) » Threads » Simple Threads
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20060503213413/http://www.java2s.com:80/Code/Java/Threads/Daemonthreadsspawnotherdaemonthreads.htm
---
Daemon threads spawn other daemon threads : Java examples (example source code) » Threads » Simple Threads

Daemon threads spawn other daemon threads

```java title=Example.java
// : c13:Daemons.java
// Daemon threads spawn other daemon threads.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Daemon extends Thread {
  private Thread[] t = new Thread[10];
  public Daemon() {
    setDaemon(true);
    start();
  }
  public void run() {
    for (int i = 0; i < t.length; i++)
      t[i] = new DaemonSpawn(i);
    for (int i = 0; i < t.length; i++)
      System.out.println("t[" + i + "].isDaemon() = " + t[i].isDaemon());
    while (true)
      yield();
  }
}
class DaemonSpawn extends Thread {
  public DaemonSpawn(int i) {
    start();
    System.out.println("DaemonSpawn " + i + " started");
  }
  public void run() {
    while (true)
      yield();
  }
}
public class Daemons {
  public static void main(String[] args) throws Exception {
    Thread d = new Daemon();
    System.out.println("d.isDaemon() = " + d.isDaemon());
    // Allow the daemon threads to
    // finish their startup processes:
    Thread.sleep(1000);
  }
} ///:~
```

Related examples in the same category
---
1. Thread Reminder
2. Thread Race Demo
3. Suggesting when to switch threads with yield()
4. Creating threads with inner classes
5. The safe way to stop a thread
6. Calling sleep() to wait for a while
7. Understanding join()
8. Daemon threads don't prevent the program from ending.
9. Shows the use of thread priorities.
10. Java new feature: threading
11. Java 1.5 (5.0) new feature: Thread Schedule
12. Two simple threads
13. Simple threads creator
14. Task
15. SimpleThread using the Runnable interface.
16. Very simple Threading example.
17. Test Override Thread
18. Test Override
19. Parallelizing Loops for Multiprocessor Machines
20. Three Threads Test
