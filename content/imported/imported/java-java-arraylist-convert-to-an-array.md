---
title: Java ArrayList convert to an array
nav: Java ArrayList convert to ...
description: String ia[] = newString[al.size()]; //define an array with the proper size
section: Imported
order: 20014
source: http://www.java2s.com/ref/java/java-arraylist-convert-to-an-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To convert an ArrayList into an array in Java

```java title=Example.java
String ia[] = newString[al.size()];  //define an array with the proper size
ia = al.toArray(ia);   //call toArray() from arrayList
```

Full source

```java title=Example.java
import java.util.ArrayList;
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String args[]) {
    // Create an array list. ArrayList<String> al = newArrayList<String>();
     //www.java2s.com// Add elements to the array list.
    al.add("SQL");
    al.add("Java");
    al.add("Javascript");
    al.add("CSS");
    al.add("HTML");
    al.add("Demo2s.com");
    al.add(1, "Hi");

    System.out.println(al);

    // Get the array. String ia[] = newString[al.size()];
    ia = al.toArray(ia);

    System.out.println(Arrays.toString(ia));
  }
}
```

PreviousNext

## Related

- Java ArrayList add element by position
- Java ArrayList add elements
- Java ArrayList check capacity
- Java ArrayList convert to array
- Java ArrayList convert to Stream
