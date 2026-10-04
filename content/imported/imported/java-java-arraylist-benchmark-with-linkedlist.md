---
title: Java ArrayList benchmark with LinkedList
nav: Java ArrayList benchmark w...
description: watch.totalTime("Array List addAll() = ");// 101,16719 Nanoseconds
section: Imported
order: 20013
source: http://www.java2s.com/ref/java/java-arraylist-benchmark-with-linkedlist.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java ArrayList benchmark with LinkedList

```java title=Example.java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

publicclass Main {
   privatestaticfinalint MAX = 500000;
   String[] strings = maxArray();

   publicstaticvoid main(String[] argv) {
      Main main = new Main();
      main.arrayListAdd();//fromwww.java2s.com
      main.linkedListAddAll();

      main.arrayListInsertOne();
      main.arrayListRemove();
      main.arrayListSearch();
   }

   publicvoid arrayListAddAll() {
      Watch watch = new Watch();
      List<String> stringList = Arrays.asList(strings);
      List<String> arrayList = newArrayList<String>(MAX);

      watch.start();
      arrayList.addAll(stringList);
      watch.totalTime("Array List addAll() = ");// 101,16719 Nanoseconds
   }

   publicvoid linkedListAddAll()  {
      Watch watch = new Watch();
      List<String> stringList = Arrays.asList(strings);

      watch.start();
      List<String> linkedList = newLinkedList<String>();
      linkedList.addAll(stringList);
      watch.totalTime("Linked List addAll() = "); // 2623,29291 Nanoseconds
   }

   // Note : ArrayList is 26 time faster here than LinkedList for addAll()publicvoid arrayListAdd() {
      Watch watch = new Watch();
      List<String> arrayList = newArrayList<String>(MAX);

      watch.start();
      for (String string : strings)
         arrayList.add(string);
      watch.totalTime("Array List add() = ");
   }

   publicvoid linkedListAdd() {
      Watch watch = new Watch();

      List<String> linkedList = newLinkedList<String>();
      watch.start();
      for (String string : strings)
         linkedList.add(string);
      watch.totalTime("Linked List add() = ");
   }

   // Note : ArrayList is 9 times faster than LinkedList for add sequentiallypublicvoid arrayListInsertOne() {
      Watch watch = new Watch();
      List<String> stringList = Arrays.asList(strings);
      List<String> arrayList = newArrayList<String>(MAX + MAX / 10);
      arrayList.addAll(stringList);

      String insertString0 = getString(true, MAX / 2 + 10);
      String insertString1 = getString(true, MAX / 2 + 20);
      String insertString2 = getString(true, MAX / 2 + 30);
      String insertString3 = getString(true, MAX / 2 + 40);

      watch.start();

      arrayList.add(insertString0);
      arrayList.add(insertString1);
      arrayList.add(insertString2);
      arrayList.add(insertString3);

      watch.totalTime("Array List add() = ");
   }

   publicvoid linkedListInsertOne() {
      Watch watch = new Watch();
      List<String> stringList = Arrays.asList(strings);
      List<String> linkedList = newLinkedList<String>();

      linkedList.addAll(stringList);

      String insertString0 = getString(true, MAX / 2 + 10);
      String insertString1 = getString(true, MAX / 2 + 20);
      String insertString2 = getString(true, MAX / 2 + 30);
      String insertString3 = getString(true, MAX / 2 + 40);

      watch.start();

      linkedList.add(insertString0);
      linkedList.add(insertString1);
      linkedList.add(insertString2);
      linkedList.add(insertString3);

      watch.totalTime("Linked List add = ");
   }

   // Note : LinkedList is 3000 nanosecond faster than ArrayList for insert// randomly.publicvoid arrayListRemove()  {
      Watch watch = new Watch();
      List<String> stringList = Arrays.asList(strings);
      List<String> arrayList = newArrayList<String>(MAX);

      arrayList.addAll(stringList);
      String searchString0 = getString(true, MAX / 2 + 10);
      String searchString1 = getString(true, MAX / 2 + 20);

      watch.start();
      arrayList.remove(searchString0);
      arrayList.remove(searchString1);
      watch.totalTime("Array List remove() = ");
   }

   publicvoid linkedListRemove() {
      Watch watch = new Watch();
      List<String> linkedList = newLinkedList<String>();
      linkedList.addAll(Arrays.asList(strings));

      String searchString0 = getString(true, MAX / 2 + 10);
      String searchString1 = getString(true, MAX / 2 + 20);

      watch.start();
      linkedList.remove(searchString0);
      linkedList.remove(searchString1);
      watch.totalTime("Linked List remove = ");
   }

   // Note : LinkedList is 10 millisecond faster than ArrayList while removing// item.publicvoid arrayListSearch() {
      Watch watch = new Watch();
      List<String> stringList = Arrays.asList(strings);
      List<String> arrayList = newArrayList<String>(MAX);

      arrayList.addAll(stringList);
      String searchString0 = getString(true, MAX / 2 + 10);
      String searchString1 = getString(true, MAX / 2 + 20);

      watch.start();
      arrayList.contains(searchString0);
      arrayList.contains(searchString1);
      watch.totalTime("Array List addAll() time =  ");// 186,15,704
   }

   publicvoid linkedListSearch() throwsException {
      Watch watch = new Watch();
      List<String> linkedList = newLinkedList<String>();
      linkedList.addAll(Arrays.asList(strings));

      String searchString0 = getString(true, MAX / 2 + 10);
      String searchString1 = getString(true, MAX / 2 + 20);

      watch.start();
      linkedList.contains(searchString0);
      linkedList.contains(searchString1);
      watch.totalTime("Linked List addAll() time =  ");
   }

   // Note : Linked List is 500 Milliseconds faster than ArrayListclass Watch {
      privatelong startTime;
      privatelong endTime;

      publicvoid start() {
         startTime = System.nanoTime();
      }

      privatevoid stop() {
         endTime = System.nanoTime();
      }

      publicvoid totalTime(String s) {
         stop();
         System.out.println(s + (endTime - startTime));
      }
   }

   privateString[] maxArray() {
      String[] strings = newString[MAX];
      Boolean result = Boolean.TRUE;
      for (int i = 0; i < MAX; i++) {
         strings[i] = getString(result, i);
         result = !result;
      }
      return strings;
   }

   privateString getString(Boolean result, int i) {
      returnString.valueOf(result) + i + String.valueOf(!result);
   }
}
```

PreviousNext

## Related

- Java ArrayList remove elements
- Java ArrayList trim to size
- Java ArrayList shuffle with your own method
- Java Arrays create IntStream from int array
- Java Arrays binary search an array
