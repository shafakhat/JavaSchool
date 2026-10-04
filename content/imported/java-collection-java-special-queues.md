---
title: Java Collection Tutorial - Java Special Queues
nav: Java Collection Tutorial -...
description: A blocking queue extends a queue by adding two sets of methods:
section: Imported - java2s Archive
order: 50338
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0177__Java_Special_Queues.html
---
```java title=Example.java
```

## Blocking Queues

A blocking queue extends a queue by adding two sets of methods:

- one set of methods blocks indefinitely
- another set of methods lets you specify a time period to block.

An instance of the BlockingQueue interface represents a blocking queue. The BlockingQueue interface inherits from the Queue interface.

put() and offer() methods adds an element to the tail of blocking queue. The put() method blocks indefinitely if the blocking queue is full until space becomes available in the queue. The offer() method lets you specify the time period to wait for space to become available. It returns true if the specified element was added successfully; false otherwise.

take() and poll() methods retrieve and remove the head of blocking queue. take() method blocks indefinitely if the blocking queue is empty. poll() method lets you specify a time period to wait if the blocking queue is empty; it returns null if the specified time elapses before an element became available.

The methods from the Queue interface within a BlockingQueue, behave as if you are using a Queue.

A BlockingQueue is designed to be thread-safe and can be used in a producer/consumer-like situation.

A blocking queue does not allow a null element and can be bounded or unbounded.

remainingCapacity() from BlockingQueue returns the number of elements that can be added to the blocking queue without blocking.

BlockingQueue can control the fairness when multiple threads are blocked. If a blocking queue is fair, it can pick the longest waiting thread to perform the operation. If the blocking queue is not fair, the order to pick is not specified.

The BlockingQueue interface and all its implementation classes are in the java.util.concurrent package. The following are the implementation classes for the BlockingQueue interface:

ArrayBlockingQueue backed by an array is a bounded implementation class for BlockingQueue. We can specify the fairness of the blocking queue in its constructor. By default, it is not fair.

LinkedBlockingQueue can be used as a bounded or unbounded blocking queue. It does not allow specifying a fairness rule for the blocking queue.

PriorityBlockingQueue is an unbounded implementation class for BlockingQueue. It works the same way as PriortyQueue for ordering the elements in the blocking queue and adds the blocking feature to PriorityQueue.

SynchronousQueue implements BlockingQueue and does not have any capacity. The put operation waits for the take operation to get the element. It can do handshake between two threads and exchange an object between two threads. Its isEmpty() method always returns true.

DelayQueue is an unbounded implementation class for BlockingQueue. It keeps an element until a specified delay has passed for that element. If there are more than one elements whose delay has passed, the element whose delay passed earliest will be placed at the head of the queue.

## Example

The following code shows how to use blocking queue in a producer/consumer application.

```java title=Example.java
import java.util.UUID;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
class BQProducer extends Thread {
  privatefinal BlockingQueue<String> queue;
  privatefinal String name;
  public BQProducer(BlockingQueue<String> queue, String name) {
    this.queue = queue;
    this.name = name;
  }
  @Override
  publicvoid run() {
    while (true) {
      try {
        this.queue.put(UUID.randomUUID().toString());
        Thread.sleep(4000);
      }
      catch (InterruptedException e) {
        e.printStackTrace();
        break;
      }
    }
  }
}
class BQConsumer extends Thread {
  privatefinal BlockingQueue<String> queue;
  privatefinal String name;
  public BQConsumer(BlockingQueue<String> queue, String name) {
    this.queue = queue;
    this.name = name;
  }
  @Override
  publicvoid run() {
    while (true) {
      try {
        String str = this.queue.take();
        System.out.println(name + "  took: " + str);
        Thread.sleep(3000);
      } catch (InterruptedException e) {
        e.printStackTrace();
        break;
      }
    }
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    int capacity = 5;
    boolean fair = true;
    BlockingQueue<String> queue = new ArrayBlockingQueue<>(capacity, fair);
    new BQProducer(queue, "Producer1").start();
    new BQProducer(queue, "Producer2").start();
    new BQProducer(queue, "Producer3").start();
    new BQConsumer(queue, "Consumer1").start();
    new BQConsumer(queue, "Consumer2").start();
  }
}
```

The code above generates the following result.

## Delay Queues

A DelayQueue implements the BlockingQueue interface. The elements inside DelayQueue must stay for a certain amount of time.

DelayQueue uses an interface called Delayed to get the to-be-delayed time.

The interface is in the java.util.concurrent package. Its declaration is as follows:

```java title=Example.java
publicinterface  Delayed  extends Comparable<Delayed>  {
   long  getDelay(TimeUnit timeUnit);
}
```

It extends the Comparable interface whose compareTo() method accepts a Delayed object.

The DelayQueue calls the getDelay() method of each element to get how long that element must be kept. The DelayQueue will pass a TimeUnit to this method.

When the getDelay() method returns a zero or a negative number, it is time for the element to get out of the queue.

The queue determines which one to pop out by calling the compareTo() method of the elements. This method determines the priority of an expired element to be removed from the queue.

The following code shows how to use DelayQueue.

```java title=Example.java
importstatic java.time.temporal.ChronoUnit.MILLIS;
importstatic java.util.concurrent.TimeUnit.MILLISECONDS;
import java.time.Instant;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.DelayQueue;
import java.util.concurrent.Delayed;
import java.util.concurrent.TimeUnit;
class DelayedJob implements Delayed {
  private Instant scheduledTime;
  String jobName;
  public DelayedJob(String jobName, Instant scheduledTime) {
    this.scheduledTime = scheduledTime;
    this.jobName = jobName;
  }
  @Override
  publiclong getDelay(TimeUnit unit) {
    long delay = MILLIS.between(Instant.now(), scheduledTime);
    long returnValue = unit.convert(delay, MILLISECONDS);
    return returnValue;
  }
  @Override
  publicint compareTo(Delayed job) {
    long currentJobDelay = this.getDelay(MILLISECONDS);
    long jobDelay = job.getDelay(MILLISECONDS);
    int diff = 0;
    if (currentJobDelay > jobDelay) {
      diff = 1;
    } elseif (currentJobDelay < jobDelay) {
      diff = -1;
    }
    return diff;
  }
  @Override
  public String toString() {
    String str = this.jobName + ", " + "Scheduled Time:  "
        + this.scheduledTime;
    return str;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) throws InterruptedException {
    BlockingQueue<DelayedJob> queue = new DelayQueue<>();
    Instant now = Instant.now();
    queue.put(new DelayedJob("A", now.plusSeconds(9)));
    queue.put(new DelayedJob("B", now.plusSeconds(3)));
    queue.put(new DelayedJob("C", now.plusSeconds(6)));
    queue.put(new DelayedJob("D", now.plusSeconds(1)));
    while (queue.size() > 0) {
      System.out.println("started...");
      DelayedJob job = queue.take();
      System.out.println("Job: " + job);
    }
    System.out.println("Finished.");
  }
}
```

The code above generates the following result.

## Transfer Queues

The transfer queue extends the blocking queue.

A producer passes an element to a consumer using the transfer(E element) method of the TransferQueue.

When a producer invokes transfer(E element) method, it waits until a consumer takes its element. The tryTransfer() method provides a non-blocking and a timeout version of the method.

The getWaitingConsumerCount() method returns the number of waiting consumers.

The hasWaitingConsumer() method returns true if there is a waiting consumer; otherwise, it returns false. The LinkedTransferQueue is an implementation class for the TransferQueue interface. It provides an unbounded TransferQueue.

The following code shows how to use the TransferQueue.

```java title=Example.java
import java.util.concurrent.LinkedTransferQueue;
import java.util.concurrent.TransferQueue;
import java.util.concurrent.atomic.AtomicInteger;
class TQProducer extends Thread {
  private String name;
  private TransferQueue<Integer> tQueue;
  private AtomicInteger sequence;
  public TQProducer(String name, TransferQueue<Integer> tQueue,
      AtomicInteger sequence) {
    this.name = name;
    this.tQueue = tQueue;
    this.sequence = sequence;
  }
  @Override
  publicvoid run() {
    while (true) {
      try {
        Thread.sleep(4000);
        int nextNum = this.sequence.incrementAndGet();
        if (nextNum % 2 == 0) {
          System.out.format("%s:  Enqueuing: %d%n", name, nextNum);
          tQueue.put(nextNum); // Enqueue
        } else {
          System.out.format("%s: Handing  off: %d%n", name, nextNum);
          System.out.format("%s: has  a  waiting  consumer: %b%n", name,
              tQueue.hasWaitingConsumer());
          tQueue.transfer(nextNum); // A hand off
        }
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
class TQConsumer extends Thread {
  privatefinal String name;
  privatefinal TransferQueue<Integer> tQueue;
  public TQConsumer(String name, TransferQueue<Integer> tQueue) {
    this.name = name;
    this.tQueue = tQueue;
  }
  @Override
  publicvoid run() {
    while (true) {
      try {
        Thread.sleep(3000);
        int item = tQueue.take();
        System.out.format("%s removed:  %d%n", name, item);
      }
      catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    final TransferQueue<Integer> tQueue = new LinkedTransferQueue<>();
    final AtomicInteger sequence = new AtomicInteger();
    for (int i = 0; i < 5; i++) {
      try {
        tQueue.put(sequence.incrementAndGet());
        System.out.println("Initial queue: " + tQueue);
        new TQProducer("Producer-1", tQueue, sequence).start();
        new TQConsumer("Consumer-1", tQueue).start();
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}
```

The code above generates the following result.

- « Previous
