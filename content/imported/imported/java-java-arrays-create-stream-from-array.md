---
title: Java Arrays create Stream from array
nav: Java Arrays create Stream ...
description: String[] array = {"CSS", "", "HTML", "Java", "Javascript", "demo2s.com"};
section: Imported
order: 20021
source: http://www.java2s.com/ref/java/java-arrays-create-stream-from-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays create Stream from array

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
       /*www.java2s.com*/System.out.println("strings greater than m sorted descending:"+list);

   }
}
```

PreviousNext

## Related

- Java Arrays convert two dimensional array to String for debug
- Java Arrays copy array
- Java Arrays copy CharSequence array
- Java Arrays fill array element value by index
- Java Arrays fill array from start index to end index
