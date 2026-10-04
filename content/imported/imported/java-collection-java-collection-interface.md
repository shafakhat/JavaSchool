---
title: Java Collection Tutorial - Java Collection Interface
nav: Java Collection Tutorial -...
description: The Java Collection interface is the root of the collection interface hierarchy. It defines a generic collection.
section: Imported - java2s Archive
order: 50329
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0030__Java_Collection_Interface.html
---
```java title=Example.java
« Previous
```

- Next »

The Java Collection interface is the root of the collection interface hierarchy. It defines a generic collection.

The Collections Framework does not provide an implementation for the Collection interface.

The Collection type is the most generic type of collection and we can use it as an argument type in methods.

Collection interface declares methods that are inherited by other types of collection interfaces.

## Methods from Collection interface

Methods of the Collection interface can be classified into the following categories:

- basic operations
- bulk operations
- aggregate operations
- array operations
- comparison operations

An implementation class must throw an UnsupportedOperationException for not-implemented optional methods.

## Basic Operations

Basic operations on a collection can

- get its number of elements as size
- add a new element to a collection
- remove an element from a collection
- check if an object exists in this collection
- check if the collection is empty

## Bulk Operations

Bulk operations performs operations on a collection for a group of objects. For example,

- removing all elements
- checking if a collection contains all elements from another collection
- adding all elements of a collection to another collection

## Aggregate Operations

Java Collection interface supports aggregate operations through streams.

A stream is a sequence of elements that supports sequential and parallel aggregate operations.

We can create a Stream object from a collection using the following methods from the Collection interface:

- default Stream<E> stream() gets a Stream with the collection as the source of elements.
- default Stream<E> parallelStream() gets a possibly parallel Stream with the collection as the source of elements for the Stream.

## Array Operations

Collection interface array operations convert a collection into an array. For example,

- Object[] toArray() converts the collections to an array.
- <T> T[] toArray(T[] a) converts collection to a T typed array.

## Comparison Operations

We can use comparison operations to compare two collections for equality.

- boolean equals(Object o) returns true if two collections are equal.
- int hashCode() returns the hash code for the collection.

## Example

The following code shows how to use Collection interface.

```java title=Example.java
Size = 0, Elements = []
import java.util.ArrayList;
import java.util.Collection;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Collection<String> names = new ArrayList<>();
    System.out.printf("Size = %d, Elements = %s%n", names.size(), names);
    names.add("XML");
    names.add("HTML");
    names.add("CSS");
    System.out.printf("Size   = %d, Elements   = %s%n",
        names.size(), names);
    names.remove("CSS");
    System.out.printf("Size   = %d, Elements   = %s%n",
        names.size(), names);
    names.clear();
    System.out.printf("Size   = %d, Elements   = %s%n",
        names.size(), names);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
