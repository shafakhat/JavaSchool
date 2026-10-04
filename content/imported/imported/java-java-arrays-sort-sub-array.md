---
title: Java Arrays sort sub array
nav: Java Arrays sort sub array
description: int array[] = { 1232, 3215, -1232, 6123, -3312, 8123, 3210, -1237, -3219, 4123 };
section: Imported
order: 20032
source: http://www.java2s.com/ref/java/java-arrays-sort-sub-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort sub array

```java title=Example.java
import java.util.Arrays;
publicclass Main {
  publicstaticvoid main(String[] a) {
    int array[] = { 1232, 3215, -1232, 6123, -3312, 8123, 3210, -1237, -3219, 4123 };
    //fromwww.java2s.comSystem.out.println(Arrays.toString(array));

    int startIndex = 3;
    int endIndex = 7;
    Arrays.sort(array, startIndex, endIndex);
    System.out.println(Arrays.toString(array));

  }
}
```

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) throwsException {
    int[] myArray = { 15, 2, 17, 3, 19, 11, 4, 111 };
    System.out.println(Arrays.toString(myArray));
    Arrays.sort(myArray, 2, 6);//www.java2s.comSystem.out.println(Arrays.toString(myArray));
  }
}
```

PreviousNext

## Related

- Java Arrays sort custom object via Comparable
- Java Arrays sort String array
- Java Arrays sort String array in case insensitive order
- Java Arrays sort using lambda expression as Comparator
- Java Arrays sort via Stream
