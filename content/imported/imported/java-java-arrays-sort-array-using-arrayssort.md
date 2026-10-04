---
title: Java Arrays sort array using Arrays.sort()
nav: Java Arrays sort array usi...
description: array[i] = -3 * i; //fromwww.java2s.com// Display, sort, and display the array. System.out.println("Original contents: "+Arrays.toString(array));
section: Imported
order: 20001
source: http://www.java2s.com/ref/java/java-arrays-sort-array-using-arrayssort.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Introduction

To sort Array using Arrays.sort() in Java

```java title=Example.java
Arrays.sort(array);
```

Full source

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String args[]) {
    // Allocate and initialize array. int array[] = newint[10];
    for(int i = 0; i < 10; i++)
      array[i] = -3 * i;  //fromwww.java2s.com// Display, sort, and display the array. System.out.println("Original contents: "+Arrays.toString(array));

    Arrays.sort(array);
    System.out.println("Original contents: "+Arrays.toString(array));

  }
}
```

PreviousNext

## Related

- Java Arrays search element via Stream filter()
- Java Arrays sort an array
- Java Arrays sort an array in reversed order
- Java Arrays sort array via Stream
- Java Arrays sort custom object via Comparable
