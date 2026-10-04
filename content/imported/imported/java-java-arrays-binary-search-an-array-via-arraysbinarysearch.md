---
title: Java Arrays binary search an array via Arrays.binarySearch()
nav: Java Arrays binary search ...
description: array[i] = -3 * i; /*fromwww.java2s.com*/Arrays.sort(array);
section: Imported
order: 20018
source: http://www.java2s.com/ref/java/java-arrays-binary-search-an-array-via-arraysbinarysearch.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To Binary search an array in Java

```java title=Example.java
Arrays.binarySearch(array, -9);
```

Full source

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String args[]) {
    // Allocate and initialize array. int array[] = newint[10];
    for(int i = 0; i < 10; i++)
      array[i] = -3 * i;  /*fromwww.java2s.com*/Arrays.sort(array);
    System.out.println("Original contents: "+Arrays.toString(array));

    // Binary search for -9. System.out.println("The value -9 is at location ");
    int index = Arrays.binarySearch(array, -9);

    System.out.print(index);

  }
}
```

PreviousNext

## Related

- Java ArrayList benchmark with LinkedList
- Java Arrays create IntStream from int array
- Java Arrays binary search an array
- Java Arrays compare two array for equality
- Java Arrays convert array to List
