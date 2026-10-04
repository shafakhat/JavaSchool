---
title: Scala Tutorial - Scala Variables
nav: Scala Tutorial - Scala Var...
description: In Scala, there are three ways you can define variables: val, var,and lazy val.
section: Imported - java2s Archive
order: 50074
source: https://www.java2s.com/Tutorials/Java/Scala/0020__Scala_Variables.html
---
```java title=Example.java
```

In Scala, there are three ways you can define variables: val, var,and lazy val.

Scala allows you to decide whether or not a variable is immutable (read-only) when you declare it.

## val

An immutable variable is declared with the keyword val.

This means that it is a variable that cannot be changed.

The following code creates a value with the name x and assigned with a literal number 10.

```java title=Example.java
val x= 10
```

```java title=Example.java
object Main {
  def main(args: Array[String]) {
        val x = 10
        println(x*x )
  }
}
```

x is declared as val and is an immutable variable so you cannot reassign a new value to x.

## var

Now let us declare a mutable variable.

A mutable variable is declared with keyword var like:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
    var y = 10
    y = 11
    println(y);
  }
}
```

You can reassign a new value to y as y is mutable, but you cannot reassign the variable to a different type.

Defining a variable of type Double and assigning it an Int value will work because Int numbers can be converted to Double numbers automatically:

```java title=Example.java
var z =10.5
println(z);
```

## Lazy val

Lazy val variables are calculated once, the first time the variable is accessed. Only vals can be lazy variables.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
        val x = 10e20
        println(x);
  }
}
```

- « Previous
