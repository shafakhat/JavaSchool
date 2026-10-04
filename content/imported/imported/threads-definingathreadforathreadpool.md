---
title: Defining a thread for a thread pool : Java examples (example source code) » Threads » Thread Pool
nav: Defining a thread for a th...
description: Defining a thread for a thread pool : Java examples (example source code) » Threads » Thread Pool
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20060503143830/http://www.java2s.com:80/Code/Java/Threads/Definingathreadforathreadpool.htm
---
Defining a thread for a thread pool

```java title=Example.java
import java.util.LinkedList;
class ThreadTask extends Thread {
  private ThreadPool pool;
  public ThreadTask(ThreadPool thePool) {
    pool = thePool;
  }
  public void run() {
    while (true) {
      // blocks until job
      Runnable job = pool.getNext();
      try {
        job.run();
      } catch (Exception e) {
        // Ignore exceptions thrown from jobs
        System.err.println("Job exception: " + e);
      }
    }
  }
}
public class ThreadPool {
  private LinkedList tasks = new LinkedList();
  public ThreadPool(int size) {
    for (int i = 0; i < size; i++) {
      Thread thread = new ThreadTask(this);
      thread.start();
    }
  }
  public void run(Runnable task) {
    synchronized (tasks) {
      tasks.addLast(task);
      tasks.notify();
    }
  }
  public Runnable getNext() {
    Runnable returnVal = null;
    synchronized (tasks) {
      while (tasks.isEmpty()) {
        try {
          tasks.wait();
        } catch (InterruptedException ex) {
          System.err.println("Interrupted");
        }
      }
      returnVal = (Runnable) tasks.removeFirst();
    }
    return returnVal;
  }
  public static void main(String args[]) {
    final String message[] = { "Java", "Source", "and", "Support" };
    ThreadPool pool = new ThreadPool(message.length / 2);
    for (int i = 0, n = message.length; i < n; i++) {
      final int innerI = i;
      Runnable runner = new Runnable() {
        public void run() {
          for (int j = 0; j < 25; j++) {
            System.out.println("j: " + j + ": " + message[innerI]);
          }
        }
      };
      pool.run(runner);
    }
  }
}
```

Related examples in the same category
---
1. Thread pool demo
2. Thread Pools 1
3. Thread Pools 2
4. Thread pool
5. Thread Pool 2
6. Thread Pool Test
