---
title: Scala Tutorial - Scala Functions
nav: Scala Tutorial - Scala Fun...
description: A Scala method is a part of a class that has a name and a signature. A function in Scala is a complete object that can be assigned to a variable.
section: Imported - java2s Archive
order: 50097
source: https://www.java2s.com/Tutorials/Java/Scala/2000__Scala_Functions.html
---
```java title=Example.java
```

Scala has both functions and methods.

A Scala method is a part of a class that has a name and a signature. A function in Scala is a complete object that can be assigned to a variable.

A function definition can appear anywhere in a source file.

## Function without Parameter

To define a function in Scala, use the def keyword followed by the method name and the method body as shown as follows.

```java title=Example.java
def hello() = {"Hello World!"}
```

The equal sign = is used as a separator between the method signature and the method body.

We can invoke this function using either hello() or hello.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
      def hello() = {"Hello World!"}
      println(hello );
  }
}
```

## Note

We can also include the optional return type as shown as follows.

```java title=Example.java
def hello():String = {"Hello World!"}
```

We can remove the parentheses from the method body altogether.

```java title=Example.java
def hello() = "Hello World!"
```

We can also remove the parentheses from the method signature altogether.

```java title=Example.java
def hello = "Hello World!"
```

## Function with Parameters

The following code shows how to create a function with parameters.

```java title=Example.java
def square (i:Int) = {i*i}
```

```java title=Example.java
The body of the functions are expressions,
where the final line becomes the return value of the function.
```

We can invoke this function as square(2).

```java title=Example.java
object Main {
  def main(args: Array[String]) {
      def square (i:Int) = {i*i}
      println(square(2) );
  }
}
```

We can provide multiple parameters in a function. Multiple parameters are separated by commas as illustrated in the following example.

```java title=Example.java
def add(x: Int, y: Int): Int = { x + y }
```

We can now invoke this function by passing actual parameters to the add function.

```java title=Example.java
object Main {
  def main(args: Array[String]) {
      def add(x: Int, y: Int): Int = { x + y }
      println(add(5, 5) );
  }
}
```

- « Previous
