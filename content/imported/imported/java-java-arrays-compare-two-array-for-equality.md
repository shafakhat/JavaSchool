---
title: Java Arrays compare two array for equality
nav: Java Arrays compare two ar...
description: // copy array intArray into array intArrayCopyint[] intArray = {1, 2, 3, 4, 5, 6};
section: Imported
order: 20022
source: http://www.java2s.com/ref/java/java-arrays-compare-two-array-for-equality.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays compare two array for equality

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] argv) throwsException {
    byte[] b = { 0 };
    byte[] a = { 0 };
    /*fromwww.java2s.com*/boolean res = Arrays.equals(a, b);

    System.out.println(res);
  }
}
```

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {

    // copy array intArray into array intArrayCopyint[] intArray = {1, 2, 3, 4, 5, 6};
    int[] intArrayCopy = newint[intArray.length];
    System.arraycopy(intArray, 0, intArrayCopy, 0, intArray.length);
    System.out.println(Arrays.toString(intArray));
    System.out.println(Arrays.toString(intArrayCopy));
    //fromwww.java2s.com// compare intArray and intArrayCopy for equalityboolean b = Arrays.equals(intArray, intArrayCopy);
    System.out.printf("%n%nintArray %s intArrayCopy%n",
       (b ? "==" : "!="));

    Arrays.fill(intArray, 0);

    // compare intArray and intArrayCopy for equality
    b = Arrays.equals(intArray, intArrayCopy);
    System.out.printf("%n%nintArray %s intArrayCopy%n",
       (b ? "==" : "!="));

  }
}
```

PreviousNext

## Related

- Java Arrays create IntStream from int array
- Java Arrays binary search an array
- Java Arrays binary search an array via Arrays.binarySearch()
- Java Arrays convert array to List
- Java Arrays convert array to List via Stream
