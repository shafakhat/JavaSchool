---
title: Calling sleep() to wait for a while : Java examples (example source code) » Threads » Simple Threads
nav: Calling sleep() to wait fo...
description: Calling sleep() to wait for a while : Java examples (example source code) » Threads » Simple Threads
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20060503213223/http://www.java2s.com:80/Code/Java/Threads/Callingsleeptowaitforawhile.htm
---
Calling sleep() to wait for a while : Java examples (example source code) » Threads » Simple Threads

Calling sleep() to wait for a while

```java title=Example.java
// : c13:SleepingThread.java
// Calling sleep() to wait for awhile.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class SleepingThread extends Thread {
  private int countDown = 5;
  private static int threadCount = 0;
  public SleepingThread() {
    super("" + ++threadCount);
    start();
  }
  public String toString() {
    return "#" + getName() + ": " + countDown;
  }
  public void run() {
    while (true) {
      System.out.println(this);
      if (--countDown == 0)
        return;
      try {
        sleep(100);
      } catch (InterruptedException e) {
        throw new RuntimeException(e);
      }
    }
  }
  public static void main(String[] args) throws InterruptedException {
    for (int i = 0; i < 5; i++)
      new SleepingThread().join();
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
6. Understanding join()
7. Daemon threads spawn other daemon threads
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
