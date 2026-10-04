---
title: Java Arrays sort custom object via Comparable
nav: Java Arrays sort custom ob...
description: Imported from java2s.com: Java Arrays sort custom object via Comparable
section: Imported
order: 20027
source: http://www.java2s.com/ref/java/java-arrays-sort-custom-object-via-comparable.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort custom object via Comparable

```java title=Example.java
import java.util.Arrays;

class Language implementsComparable<Language> {
  String name;//www.java2s.comint prodID;

  Language(String str, int id) {
    name = str;
    prodID = id;
  }

  publicint compareTo(Language p2) {
    return name.compareToIgnoreCase(p2.name);
  }

  publicboolean equals(Object p2) {
    return name.compareToIgnoreCase(((Language) p2).name) == 0;
  }
}

publicclass Main {
  publicstaticvoid main(String args[]) {
    Language[] prodList = {
        new Language("Java", 1),
        new Language("HTML", 6),
        new Language("CSS", 3),
        new Language("Javascript", 4) };

    for (Language p : prodList)
      System.out.printf("%-14s ID: %d\n", p.name, p.prodID);

    Arrays.sort(prodList);
    System.out.println();
    for (Language p : prodList)
      System.out.printf("%-14s ID: %d\n", p.name, p.prodID);
  }
}
```

PreviousNext

## Related

- Java Arrays sort an array in reversed order
- Java Arrays sort array using Arrays.sort()
- Java Arrays sort array via Stream
- Java Arrays sort String array
- Java Arrays sort String array in case insensitive order
