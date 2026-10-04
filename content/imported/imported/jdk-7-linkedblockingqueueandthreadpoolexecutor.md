---
title: LinkedBlockingQueue and ThreadPoolExecutor
nav: LinkedBlockingQueue and Th...
description: public static void main(String[] args) throws InterruptedException {
section: Imported - java2s Archive
order: 1088
source: https://web.archive.org/web/20130821083611/http://java2s.com/Code/Java/JDK-7/LinkedBlockingQueueandThreadPoolExecutor.htm
---
```java title=Example.java
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
public class Test {
  public static void main(String[] args) throws InterruptedException {
    BlockingQueue<Runnable> queue = new LinkedBlockingQueue<Runnable>();
    for (int i = 0; i < 10; i++) {
      final int localI = i;
      queue.add(new Runnable() {
        public void run() {
          doExpensiveOperation(localI);
        }
      });
    }
    ThreadPoolExecutor executor = new ThreadPoolExecutor(10, 10, 1000,
        TimeUnit.MILLISECONDS, queue);
    executor.prestartAllCoreThreads();
    executor.shutdown();
    executor.awaitTermination(100000, TimeUnit.SECONDS);
  }
  private static void doExpensiveOperation(int index) {
    System.out.println("Starting expensive operation " + index);
    try {
      Thread.sleep(index * 1000);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    System.out.println("Ending   expensive operation " + index);
  }
}
```

1.  Use ReentrantLock
---  ---
2.  Use ReentrantLock to coordinate
3.  Two ReentrantLock
