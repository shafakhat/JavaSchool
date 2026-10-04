---
title: Java ArrayList convert to Stream
nav: Java ArrayList convert to ...
description: // Create a list of Integer values.ArrayList<Integer> myList = newArrayList<>();
section: Imported
order: 20016
source: http://www.java2s.com/ref/java/java-arraylist-convert-to-stream.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java ArrayList convert to Stream

```java title=Example.java
import java.util.ArrayList;
import java.util.Optional;
import java.util.stream.Stream;

publicclass Main {

  publicstaticvoid main(String[] args) {

    // Create a list of Integer values.ArrayList<Integer> myList = newArrayList<>();
    myList.add(7);//www.java2s.com
    myList.add(18);
    myList.add(10);
    myList.add(24);
    myList.add(17);
    myList.add(5);

    System.out.println("Original list: " + myList);

    // Obtain a Stream to the array list.Stream<Integer> myStream = myList.stream();
  }
}
```

PreviousNext

## Related

- Java ArrayList check capacity
- Java ArrayList convert to an array
- Java ArrayList convert to array
- Java ArrayList get ArrayList size before and after remove action
- Java ArrayList print out content
