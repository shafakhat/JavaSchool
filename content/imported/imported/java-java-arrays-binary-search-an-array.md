---
title: Java Arrays binary search an array
nav: Java Arrays binary search ...
description: Arrays.sort(bArray);//fromwww.java2s.combyte searchValue = 2;
section: Imported
order: 20018
source: http://www.java2s.com/ref/java/java-arrays-binary-search-an-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays binary search an array

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    byte bArray[] = { 1, 2, 4, 5 ,6, 8,9};
    Arrays.sort(bArray);//fromwww.java2s.combyte searchValue = 2;

    int intResult = Arrays.binarySearch(bArray, searchValue);
    System.out.println("Result of binary search of 2 is : " + intResult);

    searchValue = 7;
    intResult = Arrays.binarySearch(bArray, searchValue);
    System.out.println("Result of binary search of 3 is : " + intResult);
  }
}
```

PreviousNext

## Related

- Java ArrayList shuffle with your own method
- Java ArrayList benchmark with LinkedList
- Java Arrays create IntStream from int array
- Java Arrays binary search an array via Arrays.binarySearch()
- Java Arrays compare two array for equality
