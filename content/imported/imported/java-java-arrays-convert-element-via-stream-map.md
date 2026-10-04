---
title: Java Arrays convert element via Stream map()
nav: Java Arrays convert elemen...
description: System.out.printf("Original strings: %s%n", Arrays.asList(strings));
section: Imported
order: 20020
source: http://www.java2s.com/ref/java/java-arrays-convert-element-via-stream-map.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays convert element via Stream map()

```java title=Example.java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] strings = {"CSS", "HTML", "Java", "Javascript"};

    System.out.printf("Original strings: %s%n", Arrays.asList(strings));

    // strings in upper caseList<String> list = Arrays.stream(strings)
             .map(String::toLowerCase)
             .collect(Collectors.toList());

    System.out.printf("strings:" + list);
 }
}
```

PreviousNext

## Related

- Java Arrays convert array to List via Stream
- Java Arrays convert array to Stream
- Java Arrays convert array to String for debug
- Java Arrays convert two dimensional array to String for debug
- Java Arrays copy array
