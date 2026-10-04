---
title: Scala Tutorial - Scala Functional Programming
nav: Scala Tutorial - Scala Fun...
description: Function literals allow us to have an expression of a function type that we can write in a short format without declaring a name for it.
section: Imported - java2s Archive
order: 50098
source: https://www.java2s.com/Tutorials/Java/Scala/2100__Scala_Functional_Programming.html
---
```java title=Example.java
```

Scala allows us to express functions as literals.

Function literals allow us to have an expression of a function type that we can write in a short format without declaring a name for it.

A function type could be one of the following:

- The type of a variable or parameter to which a function can be assigned
- An argument of a higher-order function taking a function parameter
- The result type of higher-order function returning a function

A function literal starts with a parenthesized comma-separated list of arguments followed by an arrow and the body of the function.

A function literal is also called an anonymous function.

Consider an add function:

```java title=Example.java
val add = (x: Int, y: Int) => x + y
```

Using the function literal you can define the add function as illustrated here:

```java title=Example.java
(x: Int, y: Int) => x + y.
```

A function literal is instantiated into objects called function values.

The function object extends one of the FunctionN traits, such as Function0, Function1, and so on up to Function22.

Depending on the number of arguments in the function, the corresponding FunctionN trait is chosen by the compiler.

For a function with two arguments, the compiler elects Function2 as the underlying type. For a function with 3 arguments compiler chooses Function3 , for a function with 4 arguments, Function4 and so on.

Because the function value is an object, it could be stored in a variable and it could be invoked using the parentheses function-call as illustrated here:

```java title=Example.java
object Main extends App {
   val add = (a: Int, b: Int) => a + b
   println(add(1, 2));
}
```

## First Class Function and Higher Order Function

Scala functions are objects.

In functional programming, functions are first-class citizens. A first-class function is a function that can be

- Assigned to variables,
- Passed as an argument to the other function
- Returned as values from the other function.

The function that takes a function as an argument or returns a function, are called higher-order functions.

## Function as Variable

Just as we can pass String, Int, and other variables, we can pass a function around like a variable.

We can define a function literal, and then assign that literal to a variable.

The following code defines a function literal that takes an Int parameter and returns a value that is twice the amount of the Int that is passed in:

```java title=Example.java
(i: Int) => { i * 2 }
```

We can now assign that function literal to a variable:

```java title=Example.java
val doubler = (i: Int) => { i * 2 }
```

The variable doubler is an instance of a function, known as a function value.

We can now invoke doubler as illustrated here:

```java title=Example.java
doubler(2)
```

doubler is an instance of the Function1 trait, which defines a function that takes one argument.

doubler is a function created using the keyword val and assigned to a variable.

## Function as Parameter

We can create a function or a method that takes a function as a parameter.

For this, first define a method that takes a function as a parameter.

```java title=Example.java
    def operation(functionparam:(Int, Int) => Int) {
        println(functionparam(4,4))
    }
```

The operation method takes one parameter named functionparam, which is a function.

The functionparam function takes two Int and returns an Int.

The operation method returns a Unit that indicates that operation method returns nothing.

Next, define a function that matches the expected signature. The following add function matches that signature, because it takes two Int arguments and returns an Int:

```java title=Example.java
val add = (x: Int, y:Int) => { x + y }
```

Now we can pass an add function into the operation method:

```java title=Example.java
object Main extends App {
    def operation(functionparam:(Int, Int) => Int) {
        println(functionparam(4,4))
    }
    val add = (x: Int, y:Int) => { x + y }
    operation(add)
}
```

Any function that matches this signature can be passed into the operation method.

```java title=Example.java
object Main extends App {
    def operation(functionparam:(Int, Int) => Int) {
        println(functionparam(4,4))
    }
    val add = (x: Int, y:Int) => { x + y }
    operation(add)
    val subtract = (x: Int, y:Int) => { x - y }
    val multiply = (x: Int, y:Int) => { x*y }
    operation(subtract)
    operation(multiply)
}
```

## Returning a Function

We can return a function from a function or method.

In order to do this, first define an anonymous function. The following code declares an anonymous function that takes a String argument and returns a String:

```java title=Example.java
(name: String) => { "hello" + " " + name }
```

Now we will define a method that returns the anonymous function that we just defined.

```java title=Example.java
def greeting() = (name: String) => {"hello" + " " + name}
```

On the left side of the = symbol you have a normal method declaration:

```java title=Example.java
def greeting()
```

On the right side of the = is a function literal:

```java title=Example.java
def greeting() = (name: String) => {"hello" + " " + name}
```

Now you can assign greeting() to a variable:

```java title=Example.java
val greet= greeting()
```

Because the anonymous function takes a String parameter name, we can pass it a name:

```java title=Example.java
object Main extends App {
    def greeting() = (name: String) => {"hello" + " " + name}
    val greet= greeting()
    println(greet("Scala"))
}
```

- « Previous
