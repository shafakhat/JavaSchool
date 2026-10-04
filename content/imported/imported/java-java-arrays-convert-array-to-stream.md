---
title: Java Arrays convert array to Stream
nav: Java Arrays convert array ...
description: // display original valuesSystem.out.printf("Original values: %s%n", Arrays.asList(values));
section: Imported
order: 20019
source: http://www.java2s.com/ref/java/java-arrays-convert-array-to-stream.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays convert array to Stream

```java title=Example.java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Integer[] values = { 2, 9, 5, 0, 3, 7, 1, 4, 8, 6 };

    // display original valuesSystem.out.printf("Original values: %s%n", Arrays.asList(values));

    Stream<Integer> s = Arrays.stream(values);
    /*fromwww.java2s.com*/List<Integer> list = s.sorted().collect(Collectors.toList());

    System.out.printf("Sorted values: %s%n", list);
  }
}
```

Process String array

```java title=Example.java
import java.util.Arrays;
import java.util.stream.Collectors;

publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] strings = { "CSS", "Java", "HTML", "Javascript", "SQL", "C++", "C" };
    // display original stringsSystem.out.printf("Original strings: %s%n", Arrays.asList(strings));

    // strings in uppercaseSystem.out.printf("strings in uppercase: %s%n",
        Arrays.stream(strings).map(String::toUpperCase).collect(Collectors.toList()));

    // strings less than "n" (case insensitive) sorted ascendingSystem.out.printf("strings greater than m sorted ascending: %s%n",
        Arrays.stream(strings).filter(s -> s.compareToIgnoreCase("n") < 0).sorted(String.CASE_INSENSITIVE_ORDER)
            .collect(Collectors.toList()));

    // strings less than "n" (case insensitive) sorted descendingSystem.out.printf("strings greater than m sorted descending: %s%n",
        Arrays.stream(strings).filter(s -> s.compareToIgnoreCase("n") < 0)
            .sorted(String.CASE_INSENSITIVE_ORDER.reversed()).collect(Collectors.toList()));
  }//fromwww.java2s.com
}
```

PreviousNext

## Related

- Java Arrays compare two array for equality
- Java Arrays convert array to List
- Java Arrays convert array to List via Stream
- Java Arrays convert array to String for debug
- Java Arrays convert element via Stream map()
