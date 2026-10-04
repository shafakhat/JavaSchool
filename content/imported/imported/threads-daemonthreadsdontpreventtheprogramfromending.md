---
title: Daemon threads don't prevent the program from ending. : Java examples (example source code) » Threads » Simple Threads
nav: Daemon threads don't preve...
description: Daemon threads don't prevent the program from ending. : Java examples (example source code) » Threads » Simple Threads
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20060503213509/http://www.java2s.com:80/Code/Java/Threads/Daemonthreadsdontpreventtheprogramfromending.htm
---
Daemon threads don't prevent the program from ending.

```java title=Example.java
//: c13:SimpleDaemons.java
// Daemon threads don't prevent the program from ending.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class SimpleDaemons extends Thread {
  public SimpleDaemons() {
    setDaemon(true); // Must be called before start()
    start();
  }
  public void run() {
    while(true) {
      try {
        sleep(100);
      } catch (InterruptedException e) {
        throw new RuntimeException(e);
      }
      System.out.println(this);
    }
  }
  public static void main(String[] args) {
    for(int i = 0; i < 10; i++)
      new SimpleDaemons();
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
8. Daemon threads spawn other daemon threads
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
