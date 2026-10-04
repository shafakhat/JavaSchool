---
title: Scala Tutorial - Scala Tuples
nav: Scala Tutorial - Scala Tup...
description: A tuple is an ordered container of two or more values of same or different types.
section: Imported - java2s Archive
order: 50088
source: https://www.java2s.com/Tutorials/Java/Scala/0190__Scala_Tuples.html
---
```java title=Example.java
```

A tuple is an ordered container of two or more values of same or different types.

Unlike lists and arrays, however, there is no way to iterate through elements in a tuple.

Its purpose is only as a container for more than one value.

Tuples are useful when you need to group discrete elements and provide a generic means to structure data.

We can create a tuple in two ways:

- By writing your values separated by a comma and surrounded by a pair of parentheses
- By using a relation operator ->

## Example

The following code shows a tuple containing an Int, a Boolean, and a String using the former method.

```java title=Example.java
val tuple = (1, false, "Scala")
```

The following code shows a tuple created using a relation operator:

```java title=Example.java
val tuple2 ="title" -> "Beginning Scala"
```

Individual elements of a tuple can be accessed by its index, where the first element has an index 1.

The following code shows accessing the third element of the tuple.

```java title=Example.java
val tuple = (1, false, "Scala")
val third = tuple._3
```

- « Previous
