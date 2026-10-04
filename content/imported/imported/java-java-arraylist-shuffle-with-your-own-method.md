---
title: Java ArrayList shuffle with your own method
nav: Java ArrayList shuffle wit...
description: // generate ordered list of Number objectsArrayList<Number> list = newArrayList<>();
section: Imported
order: 20015
source: http://www.java2s.com/ref/java/java-arraylist-shuffle-with-your-own-method.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java ArrayList shuffle with your own method

```java title=Example.java
import java.util.ArrayList;

publicclass Main {
  publicstaticvoid main(String[] args) {
    // generate ordered list of Number objectsArrayList<Number> list = newArrayList<>();
    for (int i = 0; i < 15; i++) {
      list.add(i);/*www.java2s.com*/
    }

    displayList(list);

    // shuffle the list
    shuffle(list);

    displayList(list);

  }

  publicstaticvoid shuffle(ArrayList<Number> list) {
    for (int i = 0; i < list.size(); i++) {
      int randomIndex = (int)(Math.random() * list.size());
      Number temp = list.get(i);
      list.set(i, list.get(randomIndex));
      list.set(randomIndex, temp);
    }
  }

  publicstaticvoid displayList(ArrayList<Number> list) {
    for (int i = 0; i < list.size(); i++) {
      System.out.print(list.get(i) + " ");
    }
    System.out.println();
  }
}
```

PreviousNext

## Related

- Java ArrayList print out content
- Java ArrayList remove elements
- Java ArrayList trim to size
- Java ArrayList benchmark with LinkedList
- Java Arrays create IntStream from int array
