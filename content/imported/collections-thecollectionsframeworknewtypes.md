---
title: The Collections Framework New Types
nav: The Collections Framework ...
description: Imported from the java2s.com archive: The Collections Framework New Types
section: Imported - java2s Archive
order: 2487
source: https://web.archive.org/web/20140829084348/http://www.java2s.com/Tutorial/Java/0140__Collections/TheCollectionsFrameworkNewTypes.htm
---
| New types in Collections Framework |
|---|
| Deque BlockingDeque NavigableMap NavigableSet |
| The Deque Interface |
| Deque [pronounced "deck"] is short for double-ended queue. |
| java.util.Deque is a subinterface of Queue. |
| A deque is a queue that supports element insertion and removal at both ends. |
| You can also restrict the maximum number of elements in a Deque. |
| Deque can also be used as a stack. |
| Methods are available for adding, removing, and inspecting elements. |
| The ArrayDeque class is an implementation of Deque that does not impose capacity restriction. |
| ArrayDeque always grows as necessary to support new elements. |
| Using Deque as a stack |

```java title=Example.java
import java.util.ArrayDeque;
import java.util.Deque;
public class IntegerStack {
  private Deque<Integer> data = new ArrayDeque<Integer>();
  public void push(Integer element) {
    data.addFirst(element);
  }
  public Integer pop() {
    return data.removeFirst();
  }
  public Integer peek() {
    return data.peekFirst();
  }
  public String toString() {
    return data.toString();
  }
  public static void main(String[] args) {
    IntegerStack stack = new IntegerStack();
    for (int i = 0; i < 5; i++) {
      stack.push(i);
    }
    System.out.println("After pushing 5 elements: " + stack);
    int m = stack.pop();
    System.out.println("Popped element = " + m);
    System.out.println("After popping 1 element : " + stack);
    int n = stack.peek();
    System.out.println("Peeked element = " + n);
    System.out.println("After peeking 1 element : " + stack);
  }
}
java title=Example.java
After pushing 5 elements: [4, 3, 2, 1, 0]
Popped element = 4
After popping 1 element : [3, 2, 1, 0]
Peeked element = 3
After peeking 1 element : [3, 2, 1, 0]
```
