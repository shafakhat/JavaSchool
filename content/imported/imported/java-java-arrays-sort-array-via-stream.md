---
title: Java Arrays sort array via Stream
nav: Java Arrays sort array via...
description: String[] array = {"CSS", "", "HTML", "Java", "Javascript", "demo2s.com"};
section: Imported
order: 20028
source: http://www.java2s.com/ref/java/java-arrays-sort-array-via-stream.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort array via Stream

```java title=Example.java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

publicclass Main {
   publicstaticvoid main(String[] args) {
      String[] array = {"CSS", "", "HTML", "Java", "Javascript", "demo2s.com"};

       List<String> list= Arrays.stream(array)
                  .filter(s -> s.compareToIgnoreCase("Java") > 0)
                  .sorted(String.CASE_INSENSITIVE_ORDER.reversed())
                  .collect(Collectors.toList());
       //www.java2s.comSystem.out.println("strings greater than m sorted descending:"+list);

   }
}
```

PreviousNext

## Related

- Java Arrays sort an array
- Java Arrays sort an array in reversed order
- Java Arrays sort array using Arrays.sort()
- Java Arrays sort custom object via Comparable
- Java Arrays sort String array
