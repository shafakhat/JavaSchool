---
title: Add an element to specified index of Java ArrayList
nav: Add an element to specifie...
description: 1. Get the size of an arraylist after and before add and remove methods
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20090425202348/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AddanelementtospecifiedindexofJavaArrayList.htm
---
```java title=Example.java
import java.util.ArrayList;
public class Main {
  public static void main(String[] args) {
    ArrayList<String> arrayList = new ArrayList<String>();
    arrayList.add("1");
    arrayList.add("2");
    arrayList.add("3");
    arrayList.add(1, "INSERTED");
    for (String str: arrayList)
      System.out.println(str);
  }
}
/*
1
INSERTED
2
3
*/
```

1.  Get the size of an arraylist after and before add and remove methods
---  ---
2.  Use the Iterator returned from ArrayList to loop through an array list
3.  Get generic Iterator from generic ArrayList
4.  Convert an ArrayList into an array.
5.  Pre-generics example that uses a collection.
6.  shows the modern, generic form of collection classes
7.  Use set method to change the value in an array list
8.  Store user-defined objects in arraylist
9.  pass the actual object you want removed.
10.  Convert a List (ArrayList) to an Array with zero length array
11.  Convert a List (ArrayList) to an Array with full length array
12.  Remove duplicate items from an ArrayList
13.  Looping through a Collection object: while loop, iterator, and for each
14.  Append all elements of other Collection to Java ArrayList
15.  Copy all elements of Java ArrayList to an Object Array
16.  Get Size of Java ArrayList and loop through elements
17.  Get Sub List of Java ArrayList
18.  Insert all elements of other Collection to Specified Index of Java ArrayList
19.  Iterate through elements Java ArrayList using Iterator
20.  Iterate through elements Java ArrayList using ListIterator
21.  Remove all elements from Java ArrayList
22.  Remove an element from specified index of Java ArrayList
23.  Search an element of Java ArrayList
24.  Get element in an ArrayList by index
25.  Replace an element at specified index of Java ArrayList
26.  Sort elements of Java ArrayList
27.  Copy Elements of ArrayList to Java Vector
28.  Copy Elements of One Java ArrayList to Another Java ArrayList
29.  Find maxmimum element of Java ArrayList
30.  Find Minimum element of Java ArrayList
31.  Get Enumeration over Java ArrayList
32.  Get Synchronized List from Java ArrayList
33.  Perform Binary Search on Java ArrayList
34.  Replace All Elements Of Java ArrayList
35.  Replace all occurrences of specified element of Java ArrayList
36.  Reverse order of all elements of Java ArrayList
37.  Shuffle elements of Java ArrayList
38.  Swap elements of Java ArrayList
39.  Iterate through a Collection using Java Iterator
40.  Sort Java ArrayList in descending order using comparator
41.  Remove an element from Collection using Java Iterator
42.  Replace an element from ArrayList using Java ListIterator
43.  How to Convert an ArrayList into an array
44.  Sort items of an ArrayList
45.  Rotate elements of a collection
46.  Search collection element
47.  If an ArrayList contains a given item
48.  Convert Collection to ArrayList?
49.  A boolean is being stored and then retrieved from an ArrayList
50.  Traverse through ArrayList in reverse direction using Java ListIterator
51.  Traverse through ArrayList in forward direction using Java ListIterator
52.  Remove an element from ArrayList using Java ListIterator
53.  Get Previous and next index using Java ListIterator
54.  A Map implemented with ArrayLists
