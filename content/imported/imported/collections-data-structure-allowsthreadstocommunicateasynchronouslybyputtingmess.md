---
title: Allows threads to communicate asynchronously by putting messages into and reading messages out of a synchronized queue.
nav: Allows threads to communic...
description: Allows threads to communicate asynchronously by putting messages into and reading messages out of a synchronized queue.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20111124202845/http://java2s.com/Code/Java/Collections-Data-Structure/Allowsthreadstocommunicateasynchronouslybyputtingmessagesintoandreadingmessagesoutofasynchronizedqueue.htm
---
Allows threads to communicate asynchronously by putting messages into and reading messages out of a synchronized queue.

```java title=Example.java
// $Id: SynchronizedQueue.java 23 2009-11-24 21:09:08Z gabe.johnson $
//package org.six11.util.adt;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.Queue;
/**
 * This class allows threads to communicate asynchronously by putting messages into and reading
 * messages out of a synchronized queue.
 *
 * @author Gabe Johnson <johnsogg@cmu.edu>
 */
public class SynchronizedQueue<T> {
  private Queue<T> messages;
  private QueueObjectSerializer<T> defaultSerializer;
  public SynchronizedQueue() {
    messages = new LinkedList<T>();
  }
  public void add(T t) {
    synchronized (this) {
      messages.add(t);
      this.notifyAll();
    }
  }
  public Collection<T> getAll(boolean remove) {
    synchronized (this) {
      Collection<T> ret = new ArrayList<T>();
      for (T t : messages) {
        ret.add(t);
      }
      if (remove) {
        messages.clear();
      }
      return ret;
    }
  }
  public void flush(PrintWriter out, QueueObjectSerializer<T> serializer, boolean hold) {
    synchronized (this) {
      T t;
      if (hold && this.isEmpty()) {
        try {
          messages.wait(5000);
        } catch (InterruptedException ex) {
          ex.printStackTrace();
        }
      }
      while ((t = messages.poll()) != null) {
        serializer.serialize(out, t);
      }
    }
  }
  public interface QueueObjectSerializer<T> {
    public void serialize(PrintWriter writer, T t);
  }
  public QueueObjectSerializer<T> getDefaultSerializer() {
    if (defaultSerializer == null) {
      defaultSerializer = new QueueObjectSerializer<T>() {
        public void serialize(PrintWriter writer, T t) {
          writer.print(t.toString());
        }
      };
    }
    return defaultSerializer;
  }
  /**
   * @return true if there are zero items in the current message list.
   */
  public boolean isEmpty() {
    return messages.isEmpty();
  }
}
```

1.  Priority queue
---  ---
2.  Queue data structure
3.  Convert a Queue to a List
4.  Create a queue using LinkedList class
5.  Simple Queue (FIFO) based on LinkedList
6.  The Generic Queue Class
7.  Blocking Queue
8.  Circular Queue
9.  Circular Queue extends AbstractList
10.  How to extend the collections framework
11.  An unbounded {@link TransferQueue} based on linked nodes.
12.  This class implements the data structures necessary for an ArrayQueue
13.  A circular queue from mina
14.  An unbounded TransferQueue based on linked nodes.
15.  Rotating queue of fixed size.
