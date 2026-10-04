---
title: Java Collection Tutorial - Java Queues
nav: Java Collection Tutorial -...
description: A queue is a collection of objects on which operations can only be performed at two ends of the queue.
section: Imported - java2s Archive
order: 50335
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0160__Java_Queue.html
---
A queue is a collection of objects on which operations can only be performed at two ends of the queue.

A queue has two ends known as head and tail.

In the simple queue, objects are added to the tail and removed from the head and the object added first will be removed first.

Java Collections Framework supports the following types of queues.

- A simple queue allows insertion at the tail and removal from the head.
- A priority queue assigns a priority to each element and allows the element with the highest priority to be removed next from the queue.
- A delay queue adds a delay to each element and removes the element only when its delay has elapsed.
- A doubly ended queue allows for insertion and removal of its elements from the head and the tail.
- A blocking queue blocks the thread that adds elements to it when it is full and it blocks the thread removing elements from it when it is empty.
- A transfer queue is a blocking queue where a handoff of an object occurs between the producer thread and a consumer thread.
- A blocking doubly ended queue is a combination of a doubly ended queue and a blocking queue.

## Simple Queues

Simple queues are represented by an instance of the Queue interface.

A queue lets you perform three basic operations:

- Add an element from its tail
- Remove an element from its head
- Peek the element at its head

The Queue interface defines two methods for each of the three operations. One method throws an exception if the operation is not possible and the other method returns a false or null to indicate the failure.

Method  Description
---  ---
boolean add(E e)  Adds an element to the queue if it is possible. Otherwise, it throws an exception.
boolean offer(E e)  Adds an element to the queue without throwing an exception if the element cannot not be added. It returns false on failure and true on success.
E remove()  removes the head of the queue. It throws an exception if the queue is empty. This method returns the removed item.
E poll()  remove element from a Queue. it returns null if the queue is empty instead of throwing an exception.
E element()  Peek the head of the queue without removing it from the queue. It throws an exception if the queue is empty.
E peek()  Peek the queue and it returns null if the queue is empty instead of throwing an exception.

The LinkedList and PriorityQueue are two implementation classes for the Queue interface. LinkedList also implement the List interface.

Queue APIs

LinkedList APIs

Stack APIs

## Example

The following code shows how to use a LinkedList as a FIFO queue.

```java title=Example.java
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Queue<String> queue = new LinkedList<>();
    queue.add("Java");
    // offer() will work the same as add()
    queue.offer("SQL");
    queue.offer("CSS");
    queue.offer("XML");
    System.out.println("Queue: " + queue);
    // Let's remove elements until the queue is empty
while (queue.peek() != null) {
      System.out.println("Head  Element: " + queue.peek());
      queue.remove();
      System.out.println("Removed one  element from  Queue");
      System.out.println("Queue: " + queue);
    }
    System.out.println("queue.isEmpty(): " + queue.isEmpty());
    System.out.println("queue.peek(): " + queue.peek());
    System.out.println("queue.poll(): " + queue.poll());
    try {
      String str = queue.element();
      System.out.println("queue.element(): " + str);
      str = queue.remove();
      System.out.println("queue.remove(): " + str);
    } catch (NoSuchElementException e) {
      System.out.println("queue.remove(): Queue is  empty.");
    }
  }
}
```

The code above generates the following result.

- « Previous
