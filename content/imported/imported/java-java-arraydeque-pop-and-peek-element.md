---
title: Java ArrayDeque pop and peek element
nav: Java ArrayDeque pop and pe...
description: Imported from java2s.com: Java ArrayDeque pop and peek element
section: Imported
order: 20013
source: http://www.java2s.com/ref/java/java-arraydeque-pop-and-peek-element.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To pop and peek element in ArrayDeque in Java

```java title=Example.java
while(adq.peek() != null) {
   System.out.println(adq.pop() + " ");
}
```

Full source

```java title=Example.java
import java.util.ArrayDeque;

publicclass Main {
  publicstaticvoid main(String args[]) {
    ArrayDeque<String> adq = newArrayDeque<String>();
     /*www.java2s.com*/// Use an ArrayDeque like a stack.
    adq.push("CSS");
    adq.push("HTML");
    adq.push("Java");
    adq.push("Javascript");
    adq.push("SQL");

    System.out.println(adq);

    System.out.println("Popping the stack: ");

    while(adq.peek() != null) {
      System.out.println(adq.pop() + " ");
    }
  }
}
```

PreviousNext

## Related

- Java ZoneRules class
- Java AbstractList wrap another list to create custom list and reverse an unmodifiable List
- Java ArrayDeque add element
- Java ArrayList class
- Java ArrayList add element by position
