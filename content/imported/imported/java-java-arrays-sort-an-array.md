---
title: Java Arrays sort an array
nav: Java Arrays sort an array
description: int[] intArray = { 431, 1235, 931, 1230, 5433, 5345, 65345, 2543 };
section: Imported
order: 20031
source: http://www.java2s.com/ref/java/java-arrays-sort-an-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort an array

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) {
    int[] intArray = { 431, 1235, 931, 1230, 5433, 5345, 65345, 2543 };

    Arrays.sort(intArray);//www.java2s.comSystem.out.println(Arrays.toString(intArray));

    String[] stringArray = { "Java", "CSS", "HTML", "Javascript", "SQL" };

    Arrays.sort(stringArray);

    System.out.println(Arrays.toString(stringArray));

  }
}
```

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) throwsException {

    // Sort Array of bytebyte[] myArray = { 65, 62, 67, 13, 19 };
    Arrays.sort(myArray);/*www.java2s.com*/System.out.println(Arrays.toString(myArray));

    // Sort Array of charchar[] myArray2 = { 'd', 'e', 'm', '0', 's' };
    Arrays.sort(myArray2);
    System.out.println(Arrays.toString(myArray2));

    // Sort Array of shortshort[] myArray3 = { 515, 122, 700, 301, 129 };
    Arrays.sort(myArray3);
    System.out.println(Arrays.toString(myArray3));

    // Sort Array of intint[] myArray4 = { 5, 2, 7, 3, 9 };
    Arrays.sort(myArray4);
    System.out.println(Arrays.toString(myArray4));

    // Sort Array of longlong[] myArray5 = { 12, 321, 567, 366, 94};
    Arrays.sort(myArray5);
    System.out.println(Arrays.toString(myArray5));

    // Sort Array of floatfloat[] myArray6 = { 12.5f, 20.50f, 30.35f, 39.5f, 90.11f };
    Arrays.sort(myArray6);
    System.out.println(Arrays.toString(myArray6));

    // Sort Array of doubledouble[] myArray7 = { 1.45d, 10.65d, 71.25d, 93.15d, 19.75d };
    Arrays.sort(myArray7);
    System.out.println(Arrays.toString(myArray7));

  }
}
```

PreviousNext

## Related

- Java Arrays fill entire array
- Java Arrays insert element using the binary search result value
- Java Arrays search element via Stream filter()
- Java Arrays sort an array in reversed order
- Java Arrays sort array using Arrays.sort()
