---
title: Java Arrays insert element using the binary search result value
nav: Java Arrays insert element...
description: Java Arrays insert element using the binary search result value
section: Imported
order: 20024
source: http://www.java2s.com/ref/java/java-arrays-insert-element-using-the-binary-search-result-value.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays insert element using the binary search result value

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) {
    int[] array = newint[10];
    insertInOrder(array,9);//fromwww.java2s.com
    insertInOrder(array,6);
    insertInOrder(array,17);
    insertInOrder(array,28);
    insertInOrder(array,-1);
    insertInOrder(array,19);
    insertInOrder(array,7);
    insertInOrder(array,12);

    System.out.println(Arrays.toString(array));
  }
  staticint elements = 0;
  publicstaticvoid insertInOrder(int[] array, int n) {
    int pos = Arrays.binarySearch(array, 0, elements, n);
    if (pos < 0)
      pos = ~pos;
    if (pos < elements)
      System.arraycopy(array, pos, array, pos + 1, elements - pos);
    array[pos] = n;
    elements++;
  }
}
```

PreviousNext

## Related

- Java Arrays fill array element value by index
- Java Arrays fill array from start index to end index
- Java Arrays fill entire array
- Java Arrays search element via Stream filter()
- Java Arrays sort an array
