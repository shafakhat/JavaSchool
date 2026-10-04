---
title: Java Collection Tutorial - Java Navigable Set
nav: Java Collection Tutorial -...
description: A navigable set is a sorted set that lets you work with its subsets in a variety of ways.
section: Imported - java2s Archive
order: 50333
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0120__Java_Navigable_Set.html
---
```java title=Example.java
```

A navigable set is a sorted set that lets you work with its subsets in a variety of ways.

NavigableSet represents a navigable set in Java Collection Framework. The NavigableSet interface inherits from the SortedSet interface and extends SortedSet.

The NavigableSet interface can navigate the set in reverse order compared to the order defined in SortedSet.

headSet(), tailSet(), and subSet() from the NavigableSet interface accept a boolean flag to include the element at the beginning or the end of the subset boundary.

lower(), floor(), higher(), and ceiling() from the NavigableSet interface search for an element based on search criteria.

The lower() method returns the greatest element that is less than the specified element.

The floor() method returns the greatest element in the NavigableSet that is less than or equal to the specified element.

The higher() method returns the least element in the NavigableSet that is greater than the specified element.

The ceiling() method returns the least element in the NavigableSet that is greater than or equal to a specified element.

pollFirst() and pollLast() retrieve and remove the first and the last element of the NavigableSet, respectively. If the NavigableSet is empty, they return null.

The TreeSet class is one of the implementation classes for the NavigableSet interface. We can use TreeSet as a set, a sorted set, and a navigable set.

TreeSet APIs

## Example

```java title=Example.java
import java.util.NavigableSet;
import java.util.TreeSet;
publicclass Main {
  publicstaticvoid main(String[] args) {
    NavigableSet<Integer> ns = new TreeSet<>();
    ns.add(0);
    ns.add(1);
    ns.add(2);
    ns.add(3);
    ns.add(4);
    ns.add(5);
    ns.add(6);
    // Get a reverse view of the navigable set
    NavigableSet<Integer> reverseNs = ns.descendingSet();
    // Print the normal and reverse views
    System.out.println("Normal order: " + ns);
    System.out.println("Reverse order: " + reverseNs);
    NavigableSet<Integer> threeOrMore = ns.tailSet(3, true);
    System.out.println("3 or  more:  " + threeOrMore);
    System.out.println("lower(3): " + ns.lower(3));
    System.out.println("floor(3): " + ns.floor(3));
    System.out.println("higher(3): " + ns.higher(3));
    System.out.println("ceiling(3): " + ns.ceiling(3));
    System.out.println("pollFirst(): " + ns.pollFirst());
    System.out.println("Navigable Set:  " + ns);
    System.out.println("pollLast(): " + ns.pollLast());
    System.out.println("Navigable Set:  " + ns);
    System.out.println("pollFirst(): " + ns.pollFirst());
    System.out.println("Navigable Set:  " + ns);
    System.out.println("pollFirst(): " + ns.pollFirst());
    System.out.println("Navigable Set:  " + ns);
    System.out.println("pollFirst(): " + ns.pollFirst());
    System.out.println("Navigable Set:  " + ns);
    System.out.println("pollFirst(): " + ns.pollFirst());
    System.out.println("pollLast(): " + ns.pollLast());
  }
}
```

The code above generates the following result.

- « Previous
