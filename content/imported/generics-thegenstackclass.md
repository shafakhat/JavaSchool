---
title: The GenStack Class
nav: The GenStack Class
description: System.out.println("There are " + gs.size() + " items in the stack.\n");
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20090603133839/http://www.java2s.com:80/Code/Java/Generics/TheGenStackClass.htm
---
```java title=Example.java
import java.util.LinkedList;
class GenStack<E> {
  private LinkedList<E> list = new LinkedList<E>();
  public void push(E item) {
    list.addFirst(item);
  }
  public E pop() {
    return list.poll();
  }
  public E peek() {
    return list.peek();
  }
  public boolean hasItems() {
    return !list.isEmpty();
  }
  public int size() {
    return list.size();
  }
}
public class GenStackTest {
  public static void main(String[] args) {
    GenStack<String> gs = new GenStack<String>();
    gs.push("One");
    gs.push("Two");
    gs.push("Three");
    gs.push("Four");
    System.out.println("There are " + gs.size() + " items in the stack.\n");
    System.out.println("The top item is: " + gs.peek() + "\n");
    System.out.println("There are still " + gs.size() + " items in the stack.\n");
    System.out.println("Popping everything:");
    while (gs.hasItems())
      System.out.println(gs.pop());
    System.out.println("There are now " + gs.size() + " items in the stack.\n");
    System.out.println("The top item is: " + gs.peek() + "\n");
  }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Generic Data Structure
6.  Unchecked Example
7.  Generic Stack
8.  Enum and Generic
9.  Generic HashMap
10.  Foreach and generic data structure
11.  Pre generics example that uses a collection.
12.  Data structure and collections: Modern, generics version.
13.  Java generic: Generics and arrays.
14.  Collections and Data structure: the generic way
