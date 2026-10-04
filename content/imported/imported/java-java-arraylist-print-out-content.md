---
title: Java ArrayList print out content
nav: Java ArrayList print out c...
description: // Create an array list. ArrayList<String> al = newArrayList<String>();
section: Imported
order: 20015
source: http://www.java2s.com/ref/java/java-arraylist-print-out-content.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To print out ArrayList content in Java

```java title=Example.java
System.out.println(arrayListObject);
```

Full source

```java title=Example.java
import java.util.ArrayList;

publicclass Main {
  publicstaticvoid main(String args[]) {
    // Create an array list. ArrayList<String> al = newArrayList<String>();
     /*fromwww.java2s.com*/// Add elements to the array list.
    al.add("SQL");
    al.add("Java");
    al.add("Javascript");
    al.add("CSS");
    al.add("HTML");
    al.add("Demo2s.com");
    al.add(1, "Hi");

    System.out.println("Size of al after additions: " +
                       al.size());

    System.out.println(al);

    // Remove elements from the array list.
    al.remove("CSS");
    al.remove(2);

    System.out.println("Size of al after deletions: " +
                       al.size());

    System.out.println(al);
  }
}
```

PreviousNext

## Related

- Java ArrayList convert to array
- Java ArrayList convert to Stream
- Java ArrayList get ArrayList size before and after remove action
- Java ArrayList remove elements
- Java ArrayList trim to size
