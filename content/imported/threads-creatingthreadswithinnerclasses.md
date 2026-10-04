---
title: Creating threads with inner classes : Java examples (example source code) » Threads » Simple Threads
nav: Creating threads with inne...
description: Creating threads with inner classes : Java examples (example source code) » Threads » Simple Threads
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20060503213314/http://www.java2s.com:80/Code/Java/Threads/Creatingthreadswithinnerclasses.htm
---
Creating threads with inner classes

```java title=Example.java
// : c13:ThreadVariations.java
// Creating threads with inner classes.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
// Using a named inner class:
class InnerThread1 {
  private int countDown = 5;
  private Inner inner;
  private class Inner extends Thread {
    Inner(String name) {
      super(name);
      start();
    }
    public void run() {
      while (true) {
        System.out.println(this);
        if (--countDown == 0)
          return;
        try {
          sleep(10);
        } catch (InterruptedException e) {
          throw new RuntimeException(e);
        }
      }
    }
    public String toString() {
      return getName() + ": " + countDown;
    }
  }
  public InnerThread1(String name) {
    inner = new Inner(name);
  }
}
// Using an anonymous inner class:
class InnerThread2 {
  private int countDown = 5;
  private Thread t;
  public InnerThread2(String name) {
    t = new Thread(name) {
      public void run() {
        while (true) {
          System.out.println(this);
          if (--countDown == 0)
            return;
          try {
            sleep(10);
          } catch (InterruptedException e) {
            throw new RuntimeException(e);
          }
        }
      }
      public String toString() {
        return getName() + ": " + countDown;
      }
    };
    t.start();
  }
}
// Using a named Runnable implementation:
class InnerRunnable1 {
  private int countDown = 5;
  private Inner inner;
  private class Inner implements Runnable {
    Thread t;
    Inner(String name) {
      t = new Thread(this, name);
      t.start();
    }
    public void run() {
      while (true) {
        System.out.println(this);
        if (--countDown == 0)
          return;
        try {
          Thread.sleep(10);
        } catch (InterruptedException e) {
          throw new RuntimeException(e);
        }
      }
    }
    public String toString() {
      return t.getName() + ": " + countDown;
    }
  }
  public InnerRunnable1(String name) {
    inner = new Inner(name);
  }
}
// Using an anonymous Runnable implementation:
class InnerRunnable2 {
  private int countDown = 5;
  private Thread t;
  public InnerRunnable2(String name) {
    t = new Thread(new Runnable() {
      public void run() {
        while (true) {
          System.out.println(this);
          if (--countDown == 0)
            return;
          try {
            Thread.sleep(10);
          } catch (InterruptedException e) {
            throw new RuntimeException(e);
          }
        }
      }
      public String toString() {
        return Thread.currentThread().getName() + ": " + countDown;
      }
    }, name);
    t.start();
  }
}
// A separate method to run some code as a thread:
class ThreadMethod {
  private int countDown = 5;
  private Thread t;
  private String name;
  public ThreadMethod(String name) {
    this.name = name;
  }
  public void runThread() {
    if (t == null) {
      t = new Thread(name) {
        public void run() {
          while (true) {
            System.out.println(this);
            if (--countDown == 0)
              return;
            try {
              sleep(10);
            } catch (InterruptedException e) {
              throw new RuntimeException(e);
            }
          }
        }
        public String toString() {
          return getName() + ": " + countDown;
        }
      };
      t.start();
    }
  }
}
public class ThreadVariations {
  public static void main(String[] args) {
    new InnerThread1("InnerThread1");
    new InnerThread2("InnerThread2");
    new InnerRunnable1("InnerRunnable1");
    new InnerRunnable2("InnerRunnable2");
    new ThreadMethod("ThreadMethod").runThread();
  }
} ///:~
```

Related examples in the same category
---
1. Thread Reminder
2. Thread Race Demo
3. Suggesting when to switch threads with yield()
4. The safe way to stop a thread
5. Calling sleep() to wait for a while
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
