---
title: Add to end Performance compare
nav: Add to end Performance com...
description: System.out.println("time for LinkedList = " + timeList(new LinkedList()));
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20061018171335/http://www.java2s.com/Code/Java/Collections-Data-Structure/AddtoendPerformancecompareLinkListandArrayList.htm
---
Add to end Performance compare: LinkList and ArrayList

```java title=Example.java
/*
time for LinkedList = 501
time for ArrayList = 126
*/
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
public class ListDemo {
  // number of objects to add to list
  static final int SIZE = 1000000;
  static long timeList(List list) {
    long start = System.currentTimeMillis();
    Object obj = new Object();
    for (int i = 0; i < SIZE; i++) {
      // add object to the rear of the list
      list.add(obj);
    }
    return System.currentTimeMillis() - start;
  }
  public static void main(String args[]) {
    // do timing for LinkedList
    System.out.println("time for LinkedList = " + timeList(new LinkedList()));
    // do timing for ArrayList
    System.out.println("time for ArrayList = " + timeList(new ArrayList()));
  }
}
```

Related examples in the same category
---
1. Add to start Performance compare: LinkList and ArrayList
2. Convert array to list and sort
3. Shuffle a list
4. Sort a list
5. Bidirectional Traversal with ListIterator
6. Int list
7. Linked List example
8. List to array
9. List Reverse Test
10. List Search Test
