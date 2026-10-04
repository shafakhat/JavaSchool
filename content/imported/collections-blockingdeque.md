---
title: BlockingDeque
nav: BlockingDeque
description: BlockingDeque<Integer> deque = new LinkedBlockingDeque<Integer>(5);
section: Imported - java2s Archive
order: 2488
source: https://web.archive.org/web/20140829090020/http://www.java2s.com/Tutorial/Java/0140__Collections/BlockingDeque.htm
---
| A blocking deque is represented by the java.util.concurrent.BlockingDeque interface. |
|---|
| A blocking deque is a deque that waits to become non-empty before retrieving an element and waits for space to become available before storing an element. |
| A blocking deque is thread-safe and does not permit null elements. |

```java title=Example.java
import java.util.concurrent.BlockingDeque;
import java.util.concurrent.LinkedBlockingDeque;
class Producer implements Runnable {
  private String name;
  private BlockingDeque<Integer> deque;
  public Producer(String name, BlockingDeque<Integer> deque) {
    this.name = name;
    this.deque = deque;
  }
  public synchronized void run() {
    for (int i = 0; i < 10; i++) {
      try {
        deque.putFirst(i);
        System.out.println(name + " puts " + i);
        Thread.sleep(300);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
class Consumer implements Runnable {
  private String name;
  private BlockingDeque<Integer> deque;
  public Consumer(String name, BlockingDeque<Integer> deque) {
    this.name = name;
    this.deque = deque;
  }
  public synchronized void run() {
    for (int i = 0; i < 10; i++) {
      try {
        int j = deque.takeLast();
        System.out.println(name + " takes " + j);
        Thread.sleep(3000);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
public class BlockingDequeTester {
  public static void main(String[] args) {
    BlockingDeque<Integer> deque = new LinkedBlockingDeque<Integer>(5);
    Runnable producer = new Producer("Producer", deque);
    Runnable consumer = new Consumer("Consumer", deque);
    new Thread(producer).start();
    try {
      Thread.sleep(500);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    new Thread(consumer).start();
  }
}
```
