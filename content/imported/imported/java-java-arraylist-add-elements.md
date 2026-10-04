---
title: Java ArrayList add elements
nav: Java ArrayList add elements
description: // Create an array list. ArrayList<String> al = newArrayList<String>();
section: Imported
order: 20002
source: http://www.java2s.com/ref/java/java-arraylist-add-elements.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To Add elements to ArrayList in Java

```java title=Example.java

arrayList.add(your object);
```

Full source

```java title=Example.java
import java.util.ArrayList;

publicclass Main {
  publicstaticvoid main(String args[]) {
    // Create an array list. ArrayList<String> al = newArrayList<String>();
     //fromwww.java2s.com// Add elements to the array list.
    al.add("SQL");
    al.add("Java");
    al.add("Javascript");
    al.add("CSS");
    al.add("HTML");
    al.add("Demo2s.com");
    al.add(1, "Hi");

    System.out.println("Size of al after additions: " +
                       al.size());

  }
}
```

PreviousNext

## Related

- Java ArrayDeque pop and peek element
- Java ArrayList class
- Java ArrayList add element by position
- Java ArrayList check capacity
- Java ArrayList convert to an array
