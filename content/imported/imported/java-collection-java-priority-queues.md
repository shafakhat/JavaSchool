---
title: Java Collection Tutorial - Java Priority Queue
nav: Java Collection Tutorial -...
description: A priory queue is a queue in which each element has an associated priority. The element with the highest priority is removed next from the queue.
section: Imported - java2s Archive
order: 50336
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0170__Java_Priority_Queues.html
---
```java title=Example.java
« Previous
```

- Next »

A priory queue is a queue in which each element has an associated priority. The element with the highest priority is removed next from the queue.

PriorityQueue is an implementation class for an unbounded priority queue in Java Collection Framework.

We can use the Comparable interface implemented in each element as its priority.

Or we can supply a Comparator object, which will determine the priority order of the elements.

When adding a new element to a priority queue, it is positioned in the queue based on its priority.

[PriorityQueue APIs](../../../Tutorials/Java/java.util/PriorityQueue/index.html)

## Example

```java title=Example.java
import java.util.PriorityQueue;
import java.util.Queue;
/*fromwww.java2s.com*/class ComparablePerson implements Comparable<ComparablePerson> {
  privateint id;
  private String name;
  public ComparablePerson(int id, String name) {
    this.id = id;
    this.name = name;
  }
  publicint getId() {
    return id;
  }
  publicvoid setId(int id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  @Override
  publicboolean equals(Object o) {
    if (!(o instanceof ComparablePerson)) {
      return false;
    }
    ComparablePerson p = (ComparablePerson) o;
    if (this.id == p.getId()) {
      return true;
    }
    return false;
  }
  @Override
  publicint hashCode() {
    return this.id;
  }
  @Override
  public String toString() {
    return"(" + id + ", " + name + ")";
  }
  @Override
  publicint compareTo(ComparablePerson cp) {
    int cpId = cp.getId();
    String cpName = cp.getName();
    if (this.getId() < cpId) {
      return -1;
    }
    if (this.getId() > cpId) {
      return 1;
    }
    if (this.getId() == cpId) {
      return this.getName().compareTo(cpName);
    }
    // Should not reach here
return 0;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Queue<ComparablePerson> pq = new PriorityQueue<>();
    pq.add(new ComparablePerson(1, "Oracle"));
    pq.add(new ComparablePerson(4, "XML"));
    pq.add(new ComparablePerson(2, "HTML"));
    pq.add(new ComparablePerson(3, "CSS"));
    pq.add(new ComparablePerson(4, "Java"));
    System.out.println(pq);
    while (pq.peek() != null) {
      System.out.println("Head  Element: " + pq.peek());
      pq.remove();
      System.out.println("Priority  queue: " + pq);
    }
  }
}
```

The code above generates the following result.

## Note

The PriorityQueue class does not guarantee any ordering of the elements when you use an iterator.

Its toString() method uses its iterator to give you the string representation of its elements.

The following code shows how to use a Comparator object to create a priority queue for the list of ComparablePerson.

```java title=Example.java
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
//fromwww.java2s.comclass ComparablePerson implements Comparable<ComparablePerson> {
  privateint id;
  private String name;
  public ComparablePerson(int id, String name) {
    this.id = id;
    this.name = name;
  }
  publicint getId() {
    return id;
  }
  publicvoid setId(int id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  @Override
  publicboolean equals(Object o) {
    if (!(o instanceof ComparablePerson)) {
      return false;
    }
    ComparablePerson p = (ComparablePerson) o;
    if (this.id == p.getId()) {
      return true;
    }
    return false;
  }
  @Override
  publicint hashCode() {
    return this.id;
  }
  @Override
  public String toString() {
    return"(" + id + ", " + name + ")";
  }
  @Override
  publicint compareTo(ComparablePerson cp) {
    int cpId = cp.getId();
    String cpName = cp.getName();
    if (this.getId() < cpId) {
      return -1;
    }
    if (this.getId() > cpId) {
      return 1;
    }
    if (this.getId() == cpId) {
      return this.getName().compareTo(cpName);
    }
    // Should not reach here
return 0;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    int initialCapacity = 5;
    Comparator<ComparablePerson> nameComparator = Comparator
        .comparing(ComparablePerson::getName);
    Queue<ComparablePerson> pq = new PriorityQueue<>(initialCapacity,
        nameComparator);
    pq.add(new ComparablePerson(1, "Oracle"));
    pq.add(new ComparablePerson(4, "XML"));
    pq.add(new ComparablePerson(2, "HTML"));
    pq.add(new ComparablePerson(3, "CSS"));
    pq.add(new ComparablePerson(4, "Java"));
    System.out.println("Priority  queue: " + pq);
    while (pq.peek() != null) {
      System.out.println("Head  Element: " + pq.peek());
      pq.remove();
      System.out.println("Removed one  element from  Queue");
      System.out.println("Priority  queue: " + pq);
    }
  }
}
```

The code above generates the following result.

- Next »
- « Previous
