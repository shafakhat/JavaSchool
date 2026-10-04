---
title: Java Arrays sort String array in case insensitive order
nav: Java Arrays sort String ar...
description: String[] stringArray = { "java", "CSS", "html", "Javascript", "SQL" };
section: Imported
order: 20026
source: http://www.java2s.com/ref/java/java-arrays-sort-string-array-in-case-insensitive-order.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort String array in case insensitive order

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) {

    String[] stringArray = { "java", "CSS", "html", "Javascript", "SQL" };

    System.out.println(Arrays.toString(stringArray));

    Arrays.sort(stringArray);//fromwww.java2s.comSystem.out.println(Arrays.toString(stringArray));

    Arrays.sort(stringArray, String.CASE_INSENSITIVE_ORDER);
    System.out.println(Arrays.toString(stringArray));

  }
}
```

PreviousNext

## Related

- Java Arrays sort array via Stream
- Java Arrays sort custom object via Comparable
- Java Arrays sort String array
- Java Arrays sort sub array
- Java Arrays sort using lambda expression as Comparator
