---
title: Java ArrayList get ArrayList size before and after remove action
nav: Java ArrayList get ArrayLi...
description: arrayList.size();//return the current element count in an array list
section: Imported
order: 20017
source: http://www.java2s.com/ref/java/java-arraylist-get-arraylist-size-before-and-after-remove-action.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To get ArrayList size before and after remove action in Java

```java title=Example.java

arrayList.size();//return the current element count in an array list
```

Full source

```java title=Example.java
import java.util.ArrayList;

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

    System.out.println("Size of al after additions: " +
                       al.size());

    // Remove elements from the array list.
    al.remove("CSS");
    al.remove(2);

    System.out.println("Size of al after deletions: " +
                       al.size());
  }
}
```

PreviousNext

## Related

- Java ArrayList convert to an array
- Java ArrayList convert to array
- Java ArrayList convert to Stream
- Java ArrayList print out content
- Java ArrayList remove elements
