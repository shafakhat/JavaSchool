---
title: Scala Tutorial - Scala Case Classes
nav: Scala Tutorial - Scala Cas...
description: Scala can create classes that have the common stuff filled in.
section: Imported - java2s Archive
order: 50102
source: https://www.java2s.com/Tutorials/Java/Scala/3020__Scala_Case_Classes.html
---
```java title=Example.java
```

Scala can create classes that have the common stuff filled in.

Most of the time, when we define a class, we have to write the toString, hashCode, and equals methods.

Scala provides the case class mechanism for filling in these blanks, as well as support for pattern matching.

A case class provides the same facilities as a normal class, but the compiler generates toString, hashCode, and equals methods which you can override.

Case classes can be instantiated without the use of the new statement.

By default, all the parameters in the case class's constructor become properties on the case class.

## Example

Here's how to create a case class:

```java title=Example.java
case class Stuff(name:String, age: Int)
```

We can create an instance of Stuff without the keyword new:

```java title=Example.java
vals = Stuff("David", 45)
s: Stuff = Stuff(David,45)
```

Call the case class's to String method:

```java title=Example.java
s.toString
```

Stuff's equals method does a deep comparison:

```java title=Example.java
s == Stuff("David",45)
s == Stuff("David",43)
```

And the instance has properties:

```java title=Example.java
s.name
s.age
```

- « Previous
