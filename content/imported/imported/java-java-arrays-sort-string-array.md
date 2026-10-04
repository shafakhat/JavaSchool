---
title: Java Arrays sort String array
nav: Java Arrays sort String ar...
description: Imported from java2s.com: Java Arrays sort String array
section: Imported
order: 20030
source: http://www.java2s.com/ref/java/java-arrays-sort-string-array.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort String array

```java title=Example.java
import java.util.*;

publicclass Main {
    publicstaticvoid main(String[] arguments) {
        String names[] = { "A", "CSS", "R", "C++",
            "T-SQL", "HTML", "Java", "Pascal", "Javascript" };
        System.out.println("The original order:");
        for (int i = 0; i < names.length; i++) {
            System.out.println(i + ": " + names[i]);
        }//www.java2s.comSystem.out.println();
        Arrays.sort(names);
        System.out.println("The new order:");
        for (int i = 0; i < names.length; i++) {
            System.out.println(i + ": " + names[i]);
        }
        System.out.println();
    }
}
```

PreviousNext

## Related

- Java Arrays sort array using Arrays.sort()
- Java Arrays sort array via Stream
- Java Arrays sort custom object via Comparable
- Java Arrays sort String array in case insensitive order
- Java Arrays sort sub array
