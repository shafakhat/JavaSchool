---
title: Scala Tutorial - Scala Lists
nav: Scala Tutorial - Scala Lists
description: In Scala Lists, all elements have the same type like arrays, but unlike arrays, elements of a list cannot by changed by assignment.
section: Imported - java2s Archive
order: 50111
source: https://www.java2s.com/Tutorials/Java/Scala/5000__Scala_Lists.html
---
```java title=Example.java
```

In Scala Lists, all elements have the same type like arrays, but unlike arrays, elements of a list cannot by changed by assignment.

The list that has elements of type T is written as List[T].

There are two ways to create a list:

- create the list in the similar manner you create arrays
- use :: cons operator.

## Example

First we will show the more traditional approach. The following code shows how you can create an empty list.

```java title=Example.java
val empty: List[Nothing] = List()
```

Note that the type of the list is Nothing.

We can create the list of books as shown in the following code:

```java title=Example.java
val books: List[String] = List("Scala", "Groovy", "Java")
```

Both these lists can be defined using a tail Nil and ::.

Nil also represents the empty list.

An empty list can be defined using Nil.

```java title=Example.java
val empty = Nil
```

The books list can be defined using a tail Nil and :: as shown in the following code.

```java title=Example.java
val books = "Scala" :: ("Groovy" :: ("Java" :: Nil))
```

The operations on the lists can be expressed in terms of head and tail methods, where head returns the first element of a list and tail returns a list consisting of all elements except the first element.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    val books = "Scala" :: ("Groovy" :: ("Java" :: Nil))
    println(books.head )
    println(books.tail )
  }
}
```

- « Previous
