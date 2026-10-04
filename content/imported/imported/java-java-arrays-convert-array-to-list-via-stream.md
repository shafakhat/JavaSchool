---
title: Java Arrays convert array to List via Stream
nav: Java Arrays convert array ...
description: // display original valuesSystem.out.printf("Original values: %s%n", Arrays.asList(values));
section: Imported
order: 20019
source: http://www.java2s.com/ref/java/java-arrays-convert-array-to-list-via-stream.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays convert array to List via Stream

```java title=Example.java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

publicclass Main {

  publicstaticvoid main(String[] args) {
    Integer[] values = {12, 19, 5, 10, 3, 17, 1, 4, 8, 6};

    // display original valuesSystem.out.printf("Original values: %s%n", Arrays.asList(values));

    // sort values in ascending order with streamsList<Integer> list = Arrays.stream(values)
             .sorted()//www.java2s.com
             .collect(Collectors.toList());

    System.out.println(list);
 }
}
```

PreviousNext

## Related

- Java Arrays binary search an array via Arrays.binarySearch()
- Java Arrays compare two array for equality
- Java Arrays convert array to List
- Java Arrays convert array to Stream
- Java Arrays convert array to String for debug
