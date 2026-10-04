---
title: Java ArrayDeque add element
nav: Java ArrayDeque add element
description: Imported from java2s.com: Java ArrayDeque add element
section: Imported
order: 20011
source: http://www.java2s.com/ref/java/java-arraydeque-add-element.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To add element to ArrayDeque in Java

```java title=Example.java

arrayDeque.add(object);
```

Full source

```java title=Example.java
import java.util.ArrayDeque;

publicclass Main {
  publicstaticvoid main(String args[]) {
    ArrayDeque<String> adq = newArrayDeque<String>();
     /*fromwww.java2s.com*/// Use an ArrayDeque like a stack.
    adq.push("CSS");
    adq.push("HTML");
    adq.push("Java");
    adq.push("Javascript");
    adq.push("SQL");

    System.out.println(adq);
  }
}
```

PreviousNext

## Related

- Java TemporalQuery Lambda method reference vs custom class
- Java ZoneRules class
- Java AbstractList wrap another list to create custom list and reverse an unmodifiable List
- Java ArrayDeque pop and peek element
- Java ArrayList class
