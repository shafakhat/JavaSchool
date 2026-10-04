---
title: Java Collection Tutorial - Java Collection Intro
nav: Java Collection Tutorial -...
description: Each object in a collection is called an element. Every collection contains a group of objects.
section: Imported - java2s Archive
order: 50005
source: https://www.java2s.com/Tutorials/Java/Java_Collection/index.html
---
- Next »

A collection is an object that contains a group of objects.

Each object in a collection is called an element. Every collection contains a group of objects.

Each different type of collection manages their elements in its own way.

The Collections Framework consists of interfaces, implementation classes, and some utility classes to handle most types of collections.

Java Collections are designed to work only with objects.

All collection classes in Java are declared generic.

## Architecture of the Collection Framework

The Java Collections Framework has three main components:

- Interfaces
- Implementation Classes
- Algorithm Classes

An interface in Java Collections Framework represents a specific type of collection.

For example, the List interface represents a list. The Set interface represents a set. The Map interface represents a map.

The data structures defined by interfaces rather than a class has the following advantages: we can provide different implementation for the same interfaces.

The Java Collections Framework also provides implementations of collection interfaces.

We should always try to define the type of the class using interfaces, rather than using their implementation classes.

The following code shows how to use the implementation class ArrayList to create a list:

```java title=Example.java
List<String> names = new ArrayList<>();
```

If possible we should avoid using the following way to create a list object.

```java title=Example.java
ArrayList<String> names = new ArrayList<>();
```

## Operations

We can perform different actions on a collection.

- searching through a collection
- converting a collection of one type to another type
- copying elements from one collection to another
- sorting elements of a collection in a specific order

- Next »
