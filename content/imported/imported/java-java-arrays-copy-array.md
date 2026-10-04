---
title: Java Arrays copy array
nav: Java Arrays copy array
description: // copy array intArray into array intArrayCopyint[] intArray = {1, 2, 3, 4, 5, 6};
section: Imported
order: 20023
source: http://www.java2s.com/ref/java/java-arrays-copy-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays copy array

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {

    // copy array intArray into array intArrayCopyint[] intArray = {1, 2, 3, 4, 5, 6};
    int[] intArrayCopy = newint[intArray.length];
    System.arraycopy(intArray, 0, intArrayCopy, 0, intArray.length);
    System.out.println(Arrays.toString(intArray));
    System.out.println(Arrays.toString(intArrayCopy));

  }/*fromwww.java2s.com*/
}
```

PreviousNext

## Related

- Java Arrays convert array to String for debug
- Java Arrays convert element via Stream map()
- Java Arrays convert two dimensional array to String for debug
- Java Arrays copy CharSequence array
- Java Arrays create Stream from array
