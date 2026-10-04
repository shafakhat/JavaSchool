---
title: Java Collection Tutorial - Java Lists
nav: Java Collection Tutorial -...
description: A list is an ordered collection of objects, defined in List interface. List interface represents a list in the Collections Framework.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Collection/0130__Java_List.html
---
A list is an ordered collection of objects, defined in List interface. List interface represents a list in the Collections Framework.

A list can have duplicate elements. and we can store multiple null values in a list.

The List interface inherits the Collection interface and it adds methods to support access to its elements using indexes.

We can add an element to the end of the List or at any position identified by an integer index.

The index of an element in a List is zero-based.

We can use the following methods to add, get, remove, and replace its elements using indexes.

```java title=Example.java
its add(int index, E  element),
addAll(int  index, Collection<? extends E> c),
get(int index),
remove(int index)
set(int  index, E  element)
```

We can search for the position of an element in the List using indexOf(Object o) or lastIndexOf(Object o) methods.

The indexOf() method searches for the specified object from the beginning and it returns the index of the first occurrence of the object.

The lastIndexOf() method searches element from the end of the list. Both methods return
-1 if the List does not contain the specified object.

subList(int fromIndex, int toIndex) returns a sublist of the original list starting at index fromIndex (inclusive) to index toIndex (exclusive).

ListIterator returned from List interface can iterate over its elements in both forward and backward directions.

List APIs

## ArrayList vs LinkedList

The following are two classes which implements the List interface:

- ArrayList
- LinkedList

An ArrayList is backed up by an array. A LinkedList is backed up by a linked list.

An ArrayList performs better if we access the elements of the list frequently. Accessing elements in an ArrayList is faster since it is array backended.

Adding or removing elements from ArrayList is slower unless done from the end, because an ArrayList has to perform an array copy internally to keep the elements in sequence.

The LinkedList performs better than ArrayList for adding and removing elements from the middle of the list. However, it is slower for accessing elements of the list, unless at the head of the list.

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
public class Main {
  public static void main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Java");
    list.add("Oracle");
    list.add("CSS");
    list.add("XML");
    System.out.println("List: " + list);
    int count = list.size();
    System.out.println("Size of  List: " + count);
    // Print each element with its index
 for (int i = 0; i < count; i++) {
      String element = list.get(i);
      System.out.println("Index=" + i + ", Element=" + element);
    }
    List<String> subList = list.subList(1, 3);
    System.out.println(subList);
    // Remove "CSS" from the list
    list.remove("CSS"); // Same as list.remove(2);
     System.out.println(list);
  }
}
```

The code above generates the following result.

ArrayList APIs

LinkedList APIs

## ListIterator

We can use ListIterator interface to iterate over a list.

The ListIterator interface inherits the Iterator interface and it adds a few more methods to access elements in the list from the current position in the backward direction.

The following code shows how to get a list iterator from a list:

```java title=Example.java
ListIterator<String> fullIterator = list.listIterator();
```

To get a list iterator starting at index 5 in the forward direction, use the following code.

```java title=Example.java
ListIterator<String> partialIterator = list.listIterator(5);
```

The following code shows how to use the ListIterator.

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;
public class Main {
  public static void main(String[] args) {
    List<String> list = new ArrayList<>();
    list.add("Oracle");
    list.add("SQL");
    list.add("CSS");
    list.add("XML");
    System.out.println("List: " + list);
    // Get the list iterator
    ListIterator<String> iterator = list.listIterator();
    while (iterator.hasNext()) {
      int index = iterator.nextIndex();
      String element = iterator.next();
      System.out.println("Index=" + index + ", Element=" + element);
    }
    // Reuse the iterator to iterate from the end to the beginning
 while (iterator.hasPrevious()) {
      int index = iterator.previousIndex();
      String element = iterator.previous();
      System.out.println("Index=" + index + ",  Element=" + element);
    }
  }
}
```

The code above generates the following result.

A ListIterator can look ahead or look back in a List.

The next() method moves one index forward and the previous() method moves one index backward.

If you use its next() method followed by the previous() method, the iterator goes back to the same position.

ListIterator APIs

- « Previous
