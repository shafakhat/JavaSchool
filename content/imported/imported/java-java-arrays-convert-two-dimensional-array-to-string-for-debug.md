---
title: Java Arrays convert two dimensional array to String for debug
nav: Java Arrays convert two di...
description: Java Arrays convert two dimensional array to String for debug
section: Imported
order: 20000
source: http://www.java2s.com/ref/java/java-arrays-convert-two-dimensional-array-to-string-for-debug.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays convert two dimensional array to String for debug

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String args[]) {
    double d [][]= {
        {0.51, 0.21,  0.23, 0.34},//fromwww.java2s.com
        {0.52, 1.12,  0.53, 0.84},
        {0.53, 0.73,  0.43},
        {0.53, 0.73,  0.43},
        {0.53, 0.73,  0.43},
        {0.53, 0.73,  0.43},
        {0.54, 0.74},
        {0.55},
    };
    System.out.println(Arrays.deepToString(d));
  }
}
```

PreviousNext

## Related

- Java Arrays convert array to Stream
- Java Arrays convert array to String for debug
- Java Arrays convert element via Stream map()
- Java Arrays copy array
- Java Arrays copy CharSequence array
