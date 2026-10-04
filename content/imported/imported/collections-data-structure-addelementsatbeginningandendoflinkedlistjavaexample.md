---
title: Add elements at beginning and end of LinkedList Java example
nav: Add elements at beginning ...
description: 2. Use addFirst method to add value to the first position in a linked list
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20090422182846/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AddelementsatbeginningandendofLinkedListJavaexample.htm
---
Add elements at beginning and end of LinkedList Java example

```java title=Example.java
import java.util.LinkedList;
public class Main {
  public static void main(String[] args) {
    LinkedList<String> lList = new LinkedList<String>();
    lList.add("1");
    lList.add("2");
    lList.add("3");
    lList.add("4");
    lList.add("5");
    System.out.println(lList);
    lList.addFirst("0");
    System.out.println(lList);
    lList.addLast("6");
    System.out.println(lList);
  }
}
/*
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
*/
```

1.  Use for each loop to go through elements in a linkedlist
---  ---
2.  Use addFirst method to add value to the first position in a linked list
3.  To insert an object into a specific position into the list, specify the index in the add method
4.  Updating LinkedList Items
5.  Convert LinkedList to Array with zero length array
6.  Convert LinkedList to Array with full length array
7.  Checking what item is first in line without removing it: element
8.  Removing the first item from the queue: poll
9.  Convert a LinkedList to ArrayList
10.  Check if a particular element exists in LinkedList Java example
11.  Create an object array from elements of LinkedList Java example
12.  Get elements from LinkedList Java example
13.  Get first and last elements from LinkedList Java example
14.  Get SubList from LinkedList Java example
15.  Iterate through elements of Java LinkedList using Iterator example
16.  Remove all elements or clear LinkedList Java example
17.  Iterate through elements of Java LinkedList using ListIterator example
18.  Remove first and last elements of LinkedList Java example
19.  Remove range of elements from LinkedList Java example
20.  Remove specified element from LinkedList Java example
21.  Replace an Element of LinkedList Java example
22.  Search elements of LinkedList Java example
23.  Add or insert an element to ArrayList using Java ListIterator Example
24.  Finding an Element in a Sorted List
25.  Create a list with an ordered list of strings
26.  Search for a non-existent element
27.  Use an Iterator to cycle through a collection in the forward direction.
28.  Implementing a Queue with LinkedList
29.  Implementing a Stack
30.  Using a LinkedList in multi-thread
31.  Convert Collection to ArrayList
32.  Wrap queue to synchronize the methods
33.  Making a stack from a LinkedList
