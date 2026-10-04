---
title: Java Arrays sort using lambda expression as Comparator
nav: Java Arrays sort using lam...
description: String[] strings = { "CSS", "Java", "HTML", "css", "sql", "javac", "javascript", "SQL" };
section: Imported
order: 20002
source: http://www.java2s.com/ref/java/java-arrays-sort-using-lambda-expression-as-comparator.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort using lambda expression as Comparator

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] strings = { "CSS", "Java", "HTML", "css", "sql", "javac", "javascript", "SQL" };

    Arrays.sort(strings, (String s1, String s2) -> {
      int c = s2.length() - s1.length();
      if (c == 0)
        c = s1.compareToIgnoreCase(s2);//fromwww.java2s.comreturn c;
    });

    System.out.print(Arrays.toString(strings));
  }
}
```

```java title=Example.java
import java.util.Arrays;
import java.util.Comparator;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Integer[] myArray = { 15, 21, 17, 13, 19 };
    Arrays.sort(myArray, newComparator<Integer>() {
      @Override/*fromwww.java2s.com*/publicint compare(Integer arg0, Integer arg1) {
        return -1 * arg0.compareTo(arg1);
      }
    });
    System.out.println(Arrays.toString(myArray));

    Arrays.sort(myArray, (Integer arg0, Integer arg1) ->{
        return -1 * arg0.compareTo(arg1);
    });
    System.out.println(Arrays.toString(myArray));
  }
}
```

PreviousNext

## Related

- Java Arrays sort String array
- Java Arrays sort String array in case insensitive order
- Java Arrays sort sub array
- Java Arrays sort via Stream
- Java Arrays sort custom object via Comparator
