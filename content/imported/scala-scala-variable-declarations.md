---
title: Scala Tutorial - Scala Variable Declarations
nav: Scala Tutorial - Scala Var...
description: Scala allows you to decide whether a variable is immutable (read-only) or not (read-write) when you declare it.
section: Imported - java2s Archive
order: 50075
source: https://www.java2s.com/Tutorials/Java/Scala/0040__Scala_Variable_Declarations.html
---
```java title=Example.java
```

Scala allows you to decide whether a variable is immutable (read-only) or not (read-write) when you declare it.

An immutable "variable" is declared with the keyword val:

```java title=Example.java
val array: Array[String] = new Array(5)
```

## Example

Array elements themselves are mutable, so the elements can be modified:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     val array: Array[String] = new Array(5)
     array = new Array(2)
     array(0) = "Hello"
     println(array )
  }
}
```

## Note

A val must be initialized when it is declared.

## Mutable variable

A mutable variable is declared with the keyword var and it must also be initialized immediately.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
     var stockPrice: Double = 100.0
     stockPrice = 200.0
     println(stockPrice);
  }
}
```

## Example 2

The following code defines a Person class with immutable first and last names, but a mutable age.

```java title=Example.java
class Person(val name: String, var age: Int)
object Main {
  def main(args: Array[String]) {
     val p = new Person("Dean Wampler", 29)
     println(p.name)
     println(p.age )
     p.age = 30
     println(p.age )
  }
}
```

- « Previous
