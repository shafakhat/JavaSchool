---
title: Scala Tutorial - Scala Value Classes
nav: Scala Tutorial - Scala Val...
description: With value classes, Scala allows user-defined value classes that extend AnyVal.
section: Imported - java2s Archive
order: 50100
source: https://www.java2s.com/Tutorials/Java/Scala/3000__Scala_Value_Classes.html
---
```java title=Example.java
« Previous
```

- Next »

With value classes, Scala allows user-defined value classes that extend AnyVal.

Scala Value classes enable us to write classes on the AnyVal side of the Scala type hierarchy.

Value classes in Scala do not allocate runtime objects.

Value classes allow us to add extension methods to a type without the runtime overhead of creating instances.

This is accomplished through the definition of new AnyVal subclasses.

## Example

The following illustrates a value class definition:

```java title=Example.java

class SomeClass(val underlying: Int) extends AnyVal
```

The preceding SomeClass class has a single, public val parameter that is the underlying runtime representation.

The type at compile time is SomeClass, but at runtime, the representation is an Int.

A value class can define defs, but no vals, vars, or nested traits classes or objects.

The following code illustrates a def in the value class SomeClass.

A value class can only extend a universal trait.

```java title=Example.java

class SomeClass(val i: Int) extends AnyVal {
    def twice() = i*2
}
```

Here SomeClass is a user-defined value class that wraps the Int parameter and encapsulates a twice method.

To invoke the twice method, create the instance of the SomeClass class as follows:

```java title=Example.java

val v = new SomeClass(9)
v.twice()
```

- Next »
- « Previous
