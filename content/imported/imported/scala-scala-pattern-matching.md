---
title: Scala Tutorial - Scala Pattern Matching
nav: Scala Tutorial - Scala Pat...
description: Pattern matching allows us to make a programmatic choice between multiple conditions.
section: Imported - java2s Archive
order: 50095
source: https://www.java2s.com/Tutorials/Java/Scala/0260__Scala_Pattern_Matching.html
---
```java title=Example.java
```

Pattern matching allows us to make a programmatic choice between multiple conditions.

## Example

```java title=Example.java

object Main extends App {
    def printNum(int: Int) {
     int match {
         case 0 => println("Zero")
         case 1 => println("One")
         case _ => println("more than one")
     }
    }
    printNum(0)
    printNum(1)
    printNum(2)
}
```

The last case with the underscore _ is wildcard. It matches anything not defined in the cases above it.

The following code illustrates the example of calculating Fibonacci numbers.

```java title=Example.java

def fibonacci(in: Int): Int = in match {
 case 0 => 0
 case 1 => 1
 case n => fibonacci(n - 1) + fibonacci(n - 2)
}
```

Scala allows guards to be placed in patterns to test for particular conditions that cannot be tested in the pattern declaration itself.

Thus, we can write our Fibonacci calculator to return 0 if a negative number is passed in as in the following examples.

```java title=Example.java

def fib2(in: Int): Int = in match {
 case n if n <= 0 => 0
 case 1 => 1
 case n => fib2(n - 1) + fib2(n - 2)
}
```

## Matching Any Type

Let's consider a list of Any type of element, containing a String, a Double, an Int, and a Char.

```java title=Example.java

object Main extends App {
    val anyList= List(1, "A", 2, 2.5, 'a')
    for (m <- anyList) {
        m match {
            case i: Int => println("Integer: " + i)
            case s: String => println("String: " + s)
            case f: Double => println("Double: " + f)
            case other => println("other: " + other)
        }
    }
}
```

## Testing Data Types

The following method tests an incoming Object to see whether it's a String, an Integer, or something else.

```java title=Example.java

def test2(in: Any) = in match {
    case s: String => "String, length "+s.length
    case i: Int if i > 0 => "Natural Int"
    case i: Int => "Another Int"
    case a: AnyRef => a.getClass.getName
    case _ => "null"
}
```

- « Previous
