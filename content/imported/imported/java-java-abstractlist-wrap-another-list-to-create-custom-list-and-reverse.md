---
title: Java AbstractList wrap another list to create custom list and reverse an unmodifiable List
nav: Java AbstractList wrap ano...
description: Java AbstractList wrap another list to create custom list and reverse an unmodifiable List
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20210102121823/http://www.java2s.com/ref/java/java-abstractlist-wrap-another-list-to-create-custom-list-and-reverse.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

```java title=Example.java
import java.util.AbstractList;
import java.util.Arrays;
import java.util.List;

publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] array = { "CSS", "HTML", "Java", "Javascript", "SQL" };

    List<String> list = Arrays.asList(array);
    System.out.println("List     : " + list);

    List<String> reversedView = reversedView(list);
    System.out.println("Reversed : " + reversedView);
  }/*fromwww.java2s.com*/publicstatic <T> List<T> reversedView(finalList<T> list) {
    returnnewAbstractList<T>() {
      @Overridepublic T get(int index) {
        return list.get(list.size() - 1 - index);
      }

      @Overridepublicint size() {
        return list.size();
      }
    };
  }
}
```

PreviousNext

## Related

- Java TemporalQuery implement to create custom query
- Java TemporalQuery Lambda method reference vs custom class
- Java ZoneRules class
- Java ArrayDeque add element
- Java ArrayDeque pop and peek element
