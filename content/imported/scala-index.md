---
title: Scala Tutorial - Scala First Scala Programs
nav: Scala Tutorial - Scala Fir...
description: We can execute Scala code by first compiling it using the scalac command line tool.
section: Imported - java2s Archive
order: 50000
source: https://www.java2s.com/Tutorials/Java/Scala/index.html
---
We can execute Scala code by first compiling it using the scalac command line tool.

```java title=Example.java
object HelloWorld {
    def main(args: Array[String]) {
        println("Hello,World!")
    }
}
```

## Note

A semicolon at the end of a statement is usually optional.

The main method is defined in an object, not in a class.

Scala program processing starts from the main method, which is a mandatory part of every Scala program.

The main method is not marked as static.

The main method is an instance method on a singleton object that is automatically instantiated.

There is no return type. Actually there is Unit, which is similar to void, but it is inferred by the compiler.

We can explicitly specify the return type by putting a colon and the type after the parameters:

```java title=Example.java
def main(args: Array[String]) : Unit = {
}
```

Scala uses the def keyword to tell the compiler that this is a method.

There is no access level modifier in Scala.

Scala does not specify the public modifier because the default access level is public.

## Printing Some Numbers

Let's write a program that will print the numbers from 1 to 10 in the Print1.scalafile:

```java title=Example.java
object Main {
  def main(args: Array[String]) {
        for {i <- 1 to10}
          println(i)
  }
}
```

We can run the code by typing scala Main.scala in the console.

The program assigns the numbers 1 to 10 to the variable and then executes println(i), which prints the numbers 1 to 10.

In the Print2.scala file, put

```java title=Example.java
object Main {
  def main(args: Array[String]) {
        for {
           i <- 1 to 10
             j <- 1 to 10
        }
        println(i* j)
  }
}
```
