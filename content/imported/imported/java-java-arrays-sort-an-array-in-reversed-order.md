---
title: Java Arrays sort an array in reversed order
nav: Java Arrays sort an array ...
description: Integer[] intArray = { 431, 1235, 931, 1230, 5433, 5345, 65345, 2543 };
section: Imported
order: 20025
source: http://www.java2s.com/ref/java/java-arrays-sort-an-array-in-reversed-order.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort an array in reversed order

```java title=Example.java
import java.util.Arrays;
import java.util.Collections;

publicclass Main {

  publicstaticvoid main(String[] args) {
    Integer[] intArray = { 431, 1235, 931, 1230, 5433, 5345, 65345, 2543 };

    System.out.println(Arrays.toString(intArray));
    Arrays.sort(intArray);/*www.java2s.com*/System.out.println(Arrays.toString(intArray));

    Arrays.sort(intArray,Collections.reverseOrder());
    System.out.println(Arrays.toString(intArray));

    String[] stringArray = { "Java", "CSS", "HTML", "Javascript", "SQL" };

    System.out.println(Arrays.toString(stringArray));
    Arrays.sort(stringArray);
    System.out.println(Arrays.toString(stringArray));

    Arrays.sort(stringArray,Collections.reverseOrder());
    System.out.println(Arrays.toString(stringArray));

  }
}
```

PreviousNext

## Related

- Java Arrays insert element using the binary search result value
- Java Arrays search element via Stream filter()
- Java Arrays sort an array
- Java Arrays sort array using Arrays.sort()
- Java Arrays sort array via Stream
