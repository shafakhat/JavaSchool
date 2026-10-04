---
title: Scala Tutorial - Scala for Loops
nav: Scala Tutorial - Scala for...
description: A For Comprehension is a very powerful control structure of Scala language.
section: Imported - java2s Archive
order: 50092
source: https://www.java2s.com/Tutorials/Java/Scala/0230__Scala_for_Loops.html
---
```java title=Example.java
```

A For Comprehension is a very powerful control structure of Scala language.

It offer the ability to iterate over a collection, and it also provides filtering options and the ability to generate new collections.

Let's start with a basic for expression:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val dogBreeds = List("A", "B", "C", "D", "E", "F")
     for (breed <- dogBreeds)
       println(breed)
  }
}
```

Basic for Expression is a very basic feature of the for expression.

First we need a collection over which the for expression will iterate. We create a list of books as shown in the following code:

```java title=Example.java
val books = List("Scala", "Groovy", "Java", "SQL", "CSS")
```

Now we can write a very basic for expression to iterate over the books list.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    val books = List("Scala", "Groovy", "Java", "SQL", "CSS")
    for (book<-books)
       println(book)
  }
}
```

In the code above the for expression creates a temporary variable called book for each element in the list books with the corresponding value of that element.

The left-arrow operator is called a generator because it generates corresponding values from a collection to be used in an expression.

## Generator Expressions

The expression breed <- dogBreeds is called a generator expression , so named because it's generating individual values from a collection.

The left arrow operator (<-) is used to iterate through a collection, such as a List.

We can also use it with a Range to write a more traditional-looking for loop:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     for (i <- 1 to 10) println(i)
  }
}
```

## Guards: Filtering Values

We can add if expressions to filter for just elements we want to keep.

These expressions are called guards.

To find all D in our list of dog breeds, we modify the previous example to the following:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val dogBreeds = List("D", "Y", "D", "S", "G", "P")
     for (breed <- dogBreeds
       if breed.contains("D")
     ) println(breed)
  }
}
```

You can have more than one guard:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val dogBreeds = List("D", "Y", "D", "S", "G", "P")
     for (breed <- dogBreeds
       if breed.contains("D")
       if  !breed.startsWith("Y")
     ) println(breed)
     for (breed <- dogBreeds
       if breed.contains("D") &&  !breed.startsWith("Y")
     ) println(breed)
  }
}
```

A filter is an if clause inside the for expression that is used to filter the collection when we do not want to iterate through the entire collection.

The following code shows how to find all Scala books in our list of books.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    val books = List("Scala", "Groovy", "Java", "SQL", "CSS")
    for(book<-books
        if book.contains("Scala")
    ) println(book)
  }
}
```

## Variable Binding

We can define variables inside for expressions.

We can then re-use these variables within the body of your for expression.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    val books = List("Scala", "Groovy", "Java", "SQL", "CSS")
    for {
        book <- books
        bookVal = book.toUpperCase()
    } println(bookVal)
  }
}
```

bookVal is not declared as a val, but you can still reuse it.

## Yielding

In Scala's for expression we can use the yield keyword to generate new collections.

The type of the collection generated from the for expression is inferred from the type of the collection being iterated over.

To hand value off to another part of our program in for loop, use the yield keyword to generating new collections with for expressions.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val dogBreeds = List("D", "Y", "D", "S", "G", "P")
     val filteredBreeds = for {
       breed <- dogBreeds
       if breed.contains("T") &&  !breed.startsWith("Y")
     } yield breed
  }
}
```

The following code shows how to use yielding for a collection.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    val books = List("Scala", "Groovy", "Java", "SQL", "CSS")
    var scalabooks = for{
        book <-books
        if book.contains("Scala")
    }yield book
    println(scalabooks);
  }
}
```

The filtered result is yielded as a value named book.

This result is accumulated with every run inside the for loop, and thus accumulated collection is assigned to the value scalabooks.

The scalabooks is of type List[String], because it is a subset of the books list, which is also of type List[String].

## Expanded Scope and Value Definitions

Scala's for comprehensions can define values inside the first part of your for expressions that can be used in the later expressions, as in this example:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val dogBreeds = List("D", "Y", "D", "S", "G", "P")
     for {
       breed <- dogBreeds
       upcasedBreed = breed.toUpperCase()
     } println(upcasedBreed)
  }
}
```

- « Previous
