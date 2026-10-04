---
title: Java Collection Tutorial - Java Collections Traversing
nav: Java Collection Tutorial -...
description: In Java Collections Framework, different types of collections store their elements differently using different types of data structures.
section: Imported - java2s Archive
order: 50330
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0040__Java_Collections_Traversing.html
---
```java title=Example.java
```

In Java Collections Framework, different types of collections store their elements differently using different types of data structures.

Some collections has ordering on their elements and some do not. The Collections Framework provides the following ways to traverse a collection:

- Using an Iterator
- Using a for-each loop
- Using the forEach() method

## Using an Iterator

A collection provides an iterator to iterate over all its elements.

An iterator can perform the following three operations on a collection:

- Check if there is an element that has not been yet accessed.
- Access the next element in the collection.
- Remove the last accessed element of the collection.

An iterator in Java is an instance of the Iterator<E> interface.

We can get an iterator for a collection using the iterator() method from the Collection interface.

The following code creates a list of strings and gets an iterator for the list:

```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
publicclass Main {
  publicstatic void main(String[] args) {
    // Create a list of strings
    List<String> names = new ArrayList<>();
    // Get an iterator for the list
    Iterator<String> nameIterator = names.iterator();
  }
}
```

The Iterator<E> interface contains the following methods:

```java title=Example.java
boolean hasNext()
E next()
default void  remove()
default void  forEachRemaining(Consumer<? super  E> action)
```

The hasNext() method returns true if there are more elements in the collection to iterate. Otherwise, it returns false.

The next() method returns the next element from the collection. We should always call the hasNext() method before calling the next() method. If not, next() method throws a NoSuchElementException.

## Example

Typically, the hasNext() and next() methods are used together in a loop. The following code prints all elements of a list using an iterator:

```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a list of strings
    List<String> names = new ArrayList<>();
    names.add("A");
    names.add("B");
    names.add("C");
    // Get an iterator for the list
    Iterator<String> nameIterator = names.iterator();
    // Iterate over all elements in the list
while (nameIterator.hasNext()) {
      // Get the next element from the list
      String name = nameIterator.next();
      System.out.println(name);
    }
  }
}
```

The code above generates the following result.

The remove() method removes the element that was returned last time by the next() method. The remove() method can be called only once per call to the next() method.

If the remove() method is called more than once for each next() method or before the first call to the next(), it throws an IllegalStateException.

The support for the remove() method is optional. The remove() method may throw an UnsupportedOperationException.

## Example 2

The following code iterates over all elements of a list using an iterator and removes the element using the remove() method.

```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a list of strings
    List<String> names = new ArrayList<>();
    names.add("A");
    names.add("B");
    names.add("C");
    Iterator<String> nameIterator = names.iterator();
    // Iterate over all elements in the list
while (nameIterator.hasNext()) {
      // Get the next element from the list
      String name = nameIterator.next();
      System.out.println(name);
      nameIterator.remove();
    }
    System.out.println(names);
  }
}
```

The code above generates the following result.

## Example 3

The forEachRemaining() method takes an action on each element of the collection that has not been accessed by the iterator yet.

The action is specified as a Consumer.

The following code shows how to print all elements of a list.

```java title=Example.java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a list of strings
    List<String> names = new ArrayList<>();
    names.add("A");
    names.add("B");
    names.add("C");
    Iterator<String> nameIterator = names.iterator();
    nameIterator.forEachRemaining(System.out::println);
  }
}
```

The code above generates the following result.

## Note for Iterator

An Iterator is a one-time object. We cannot reset an iterator and it cannot be reused.

To iterate over the elements of the same collection again, create a new Iterator by calling the iterator() method of the collection.

## Using a for-each Loop

We can use the for-each loop to iterate over elements of a collection.

We can use the for-each loop to iterate over any collection whose implementation class implements the Iterable interface.

The general syntax for the for-each loop is as follows:

```java title=Example.java
Collection<T> yourCollection  = ;
for(T  element : yourCollection)  {
}
```

Behind the scenes, for-each loop gets the iterator and calls the hasNext() and next() methods.

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a list of strings
    List<String> names = new ArrayList<>();
    names.add("A");
    names.add("B");
    names.add("C");
    for (String name : names) {
      System.out.println(name);
    }
  }
}
```

The code above generates the following result.

## Note for for-each

The for-each loop has several limitations.

We cannot use the for-each loop to remove elements from the collection.

The following code will throw a ConcurrentModificationException exception:

```java title=Example.java
List<String> names = get   a  list;
for(String name : names)  {
    names.remove(name);// Throws a  ConcurrentModificationException
}
```

With for-each loop we have no way to start from middle of the collection.

The for-each loop provides no way to visit the previously visited elements.

## Using the forEach() Method

The Iterable interface contains a new forEach(Consumer action) method.

The method iterates over all elements and applies the action.

The forEach() method is available in all collection types that inherit from the Collection interface.

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a list of strings
    List<String> names = new ArrayList<>();
    names.add("A");
    names.add("B");
    names.add("C");
    names.forEach(System.out::println);
  }
}
```

The code above generates the following result.

- « Previous
