---
title: Add or insert an element to ArrayList using Java ListIterator Example
nav: Add or insert an element t...
description: Add or insert an element to ArrayList using Java ListIterator Example
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20090422182851/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AddorinsertanelementtoArrayListusingJavaListIteratorExample.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.ListIterator;
public class Main {
  public static void main(String[] args) {
    ArrayList<String> aList = new ArrayList<String>();
    aList.add("1");
    aList.add("2");
    aList.add("3");
    aList.add("4");
    aList.add("5");
    ListIterator<String> listIterator = aList.listIterator();
    listIterator.next();
    listIterator.add("Added Element");
    for (String str: aList){
      System.out.println(str);
    }
  }
}
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
10.  Add elements at beginning and end of LinkedList Java example
11.  Check if a particular element exists in LinkedList Java example
12.  Create an object array from elements of LinkedList Java example
13.  Get elements from LinkedList Java example
14.  Get first and last elements from LinkedList Java example
15.  Get SubList from LinkedList Java example
16.  Iterate through elements of Java LinkedList using Iterator example
17.  Remove all elements or clear LinkedList Java example
18.  Iterate through elements of Java LinkedList using ListIterator example
19.  Remove first and last elements of LinkedList Java example
20.  Remove range of elements from LinkedList Java example
21.  Remove specified element from LinkedList Java example
22.  Replace an Element of LinkedList Java example
23.  Search elements of LinkedList Java example
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
