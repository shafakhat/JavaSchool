---
title: Java ArrayList trim to size
nav: Java ArrayList trim to size
description: The trimToSize() method makes sure that there is no unused space in the underline data structure for ArrayList.
section: Imported
order: 20017
source: http://www.java2s.com/ref/java/java-arraylist-trim-to-size.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

The trimToSize() method makes sure that there is no unused space in the underline data structure for ArrayList.

```java title=Example.java
import java.util.ArrayList;

publicclass Main {
  publicstaticvoid main(String[] a) {

    ArrayList<String> list = newArrayList<>();
    System.out.println(list.size());
    //fromwww.java2s.com
    list.ensureCapacity(200);
    for(int i=0;i<100;i++) {
      list.add("A");
    }

    System.out.println(list);

    list.trimToSize();

  }
}
```

PreviousNext

## Related

- Java ArrayList get ArrayList size before and after remove action
- Java ArrayList print out content
- Java ArrayList remove elements
- Java ArrayList shuffle with your own method
- Java ArrayList benchmark with LinkedList
