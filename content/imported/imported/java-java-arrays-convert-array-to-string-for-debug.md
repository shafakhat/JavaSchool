---
title: Java Arrays convert array to String for debug
nav: Java Arrays convert array ...
description: Imported from java2s.com: Java Arrays convert array to String for debug
section: Imported
order: 20016
source: http://www.java2s.com/ref/java/java-arrays-convert-array-to-string-for-debug.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays convert array to String for debug

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String args[]) {
    String s[] = {"CSS", "HTML", "css", "demo2s.com"};

    System.out.println(Arrays.toString(s));
  }/*www.java2s.com*/
}
```

PreviousNext

## Related

- Java Arrays convert array to List
- Java Arrays convert array to List via Stream
- Java Arrays convert array to Stream
- Java Arrays convert element via Stream map()
- Java Arrays convert two dimensional array to String for debug
