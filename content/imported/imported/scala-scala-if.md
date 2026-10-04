---
title: Scala Tutorial - Scala If
nav: Scala Tutorial - Scala If
description: The result of if/else is based on the type of each part of the expression.
section: Imported - java2s Archive
order: 50091
source: https://www.java2s.com/Tutorials/Java/Scala/0220__Scala_If.html
---
```java title=Example.java
```

The result of if expressions in Scala is always Unit.

The result of if/else is based on the type of each part of the expression.

## Example

The following code illustrates if expressions in Scala.

```java title=Example.java

if (exp) println("yes")
```

The code above prints "yes" if exp is true.

Like Java, an if expression may have a multiline code block.

```java title=Example.java

if (exp) {
    println("Line one")
    println("Line two")
}
```

The if/else in Scala behaves like the ternary operator in Java:

```java title=Example.java

val i: Int = if (exp) 1 else 3
```

and either (or both) parts of the expression may have multiline code blocks as illustrated in the following code.

```java title=Example.java

val i: Int = if (exp)
                1
             else {
                val j = System.currentTimeMillis
                (j % 100L).toInt
             }
```

- « Previous
