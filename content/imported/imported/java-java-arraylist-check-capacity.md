---
title: Java ArrayList check capacity
nav: Java ArrayList check capac...
description: The List capacity tracks the number of elements the list can hold before enlarging it.
section: Imported
order: 20012
source: http://www.java2s.com/ref/java/java-arraylist-check-capacity.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

The List capacity tracks the number of elements the list can hold before enlarging it.

We can use the ensureCapacity() method to check that the internal data structure has enough capacity before adding elements.

```java title=Example.java
import java.util.ArrayList;

publicclass Main {
  publicstaticvoid main(String[] a) {

    ArrayList<String> list = newArrayList<>();
    System.out.println(list.size());
    /*www.java2s.com*/
    list.ensureCapacity(200);
    for(int i=0;i<100;i++) {
      list.add("A");
    }

    System.out.println(list);

  }
}
```

PreviousNext

## Related

- Java ArrayList class
- Java ArrayList add element by position
- Java ArrayList add elements
- Java ArrayList convert to an array
- Java ArrayList convert to array
