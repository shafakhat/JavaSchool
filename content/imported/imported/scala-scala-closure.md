---
title: Scala Tutorial - Scala Closure
nav: Scala Tutorial - Scala Clo...
description: A closure is a function, whose return value depends on the value of one or more variables declared outside this function.
section: Imported - java2s Archive
order: 50108
source: https://www.java2s.com/Tutorials/Java/Scala/3080__Scala_Closure.html
---
```java title=Example.java
```

A closure is a function, whose return value depends on the value of one or more variables declared outside this function.

## Example

Let's create a multiplier function as illustrated:

```java title=Example.java

var y = 3
val multiplier = (x:Int) => x * y
```

Now, y has a reference to a variable outside the function but in the enclosing scope.

```java title=Example.java

object Main extends App {
    var y = 3
    val multiplier = (x:Int) => x * y
    println(multiplier(3))
}
```

## Partially Applied Function

In functional programming languages, calling a function with parameters is to apply the function to the parameters.

When all the parameters are passed to the function we have fully applied the function to all the parameters.

A simple add function:

```java title=Example.java

val add = (x: Int, y: Int) => x + y
add(1,2)
```

But when we give only a subset of the parameters to the function, the result of the expression is a partially applied function.

```java title=Example.java

val partiallyAdd = add(1, _:Int)
```

Because we haven't provided a value for the second parameter, the variable partially Add is a partially applied function.

When you give partiallyAdd an Int value 2, you get the sum of the Int number passed into the add and partiallyAdd functions:

```java title=Example.java

partiallyAdd(2)
```

When we provide all the parameters, the original function is executed, yielding the result.

## Curried Function

Currying converts a function with multiple parameters creating a chain of function, each expecting a single parameter.

The following code creates add function that adds two Int parameters, a and b, as illustrated here:

```java title=Example.java

val add = (x: Int, y: Int) => x + y
add(3,3)
```

In Scala, curried functions are defined with multiple parameter lists, as follows:

```java title=Example.java

def add(x: Int)(y: Int) = x + y
```

We can also use the following syntax to define a curried function:

```java title=Example.java

def add(x: Int) = (y: Int) => x + y
```

Instead of one list of two Int parameters, you apply the curried add function to two lists of one Int parameter.

Thus the curried add function looks like this:

```java title=Example.java

def curriedAdd(a: Int)(b: Int) = a + b
curriedAdd(2)(2)
```

- « Previous
