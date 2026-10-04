---
title: Scala Tutorial - Scala Objects
nav: Scala Tutorial - Scala Obj...
description: In Scala, we can use object to refer to an instance of a class as in Java and we can also use object as a keyword.
section: Imported - java2s Archive
order: 50103
source: https://www.java2s.com/Tutorials/Java/Scala/3030__Scala_Objects.html
---
```java title=Example.java
« Previous
```

- Next »

In Scala, we can use object to refer to an instance of a class as in Java and we can also use object as a keyword.

## Singleton Objects

Scala does not have static members. Instead, Scala has singleton objects.

A singleton object definition looks like a class definition, except instead of the keyword class you use the keyword object.

A singleton is a class that can have only one instance.

For instance, we can create a singleton object to represent a Car like so:

```java title=Example.java

object Car {
   def drive {
      println("drive car")
   }
}
```

With Car defined as an object, there can be only one instance of it, and we can call its methods just like static methods on a Java class:

```java title=Example.java

Car.drive
```

Unlike classes, singleton objects cannot take parameter.

## Note

We can use singleton objects for many purposes, including collecting related utility methods, or defining an entry point to a Scala application.

There are two ways to create a launching point for your application: define an object with a properly defined main method or define an object or that extends the App trait.

For the second approach, define an object that extends the App trait as shown here:

```java title=Example.java

object Main extends App {
    println("Hello, world")
}
```

Scala provides a trait, scala.Application that your singleton object should extend for launching the application.

Then you place the code you would have put in the main method directly in the singleton object.

- Next »
- « Previous
