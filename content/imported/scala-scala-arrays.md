---
title: Scala Tutorial - Scala Arrays
nav: Scala Tutorial - Scala Arr...
description: The array is a data structure consisting of a collection of elements of the same type.
section: Imported - java2s Archive
order: 50110
source: https://www.java2s.com/Tutorials/Java/Scala/5000__Scala_Arrays.html
---
```java title=Example.java
```

The array is a data structure consisting of a collection of elements of the same type.

Elements are associated with an index, usually an integer, which is used to access or replace a particular element.

There are two ways to define an array: specify the total number of elements and then assigns values to the elements, or we can specify all values at once.

## Example

The following code shows how to create an array of Strings that may hold up to three elements.

```java title=Example.java
var books:Array[String] = new Array[String](3)
```

Here books is declared as an array of Strings that may hold up to three elements. We can simplify the declaration as follows.

```java title=Example.java
var books = new Array[String](3)
```

We can define the books array and assign values as follows.

```java title=Example.java
var books = Array("Scala", "Java", "Groovy")
```

We can assign values to individual elements or get access to individual elements, using commands shown as follows:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    var books = new Array[String](3)
    books(0) = "Scala";
    books(1) = "Java";
    books(2) = "Groovy"
    println(books(0))
  }
}
```

The index of the first element of an array is the number 0 and the index of the last element is the total number of elements minus one.

- « Previous
