---
title: Scala Tutorial - Scala Strings
nav: Scala Tutorial - Scala Str...
description: Scala's String is built on Java's String and adds additional features such as string interpolation to Java's String.
section: Imported - java2s Archive
order: 50082
source: https://www.java2s.com/Tutorials/Java/Scala/0130__Scala_Strings.html
---
```java title=Example.java
```

Scala's String is built on Java's String and adds additional features such as string interpolation to Java's String.

## Example

Following example illustrates a string literal using double quotes:

```java title=Example.java

object Main {
  def main(args: Array[String]) {
      val hello = "Hello"
      println(hello);
  }
}
```

## String Interpolation

String interpolation is a mechanism to combine values inside a string with variables.

The notation for interpolation in Scala is an s prefix added before the first double quote of the string.

Then dollar sign operator $ can be used to reference the variable.

The following code illustrates the usageof string interpolation.

```java title=Example.java

object Main {
  def main(args: Array[String]) {
      val bookTitle = "Scala" // creating a String
      // String interpolation
      println(s"Book Title is ${ bookTitle}" );
  }
}
```

- « Previous
