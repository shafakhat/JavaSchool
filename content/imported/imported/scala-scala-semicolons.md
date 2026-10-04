---
title: Scala Tutorial - Scala Semicolons
nav: Scala Tutorial - Scala Sem...
description: Scala treats the end of a line as the end of an expression, except when it can infer that the expression continues to the next line, as in this example:
section: Imported - java2s Archive
order: 50076
source: https://www.java2s.com/Tutorials/Java/Scala/0060__Scala_Semicolons.html
---
```java title=Example.java
```

Semicolons are expression delimiters and they are inferred.

Scala treats the end of a line as the end of an expression, except when it can infer that the expression continues to the next line, as in this example:

## Example

The following Trailing equals sign indicates more code on the next line.

```java title=Example.java

     def equalsign(s: String) =
       println("equalsign: " + s)
```

The following Trailing opening curly brace indicates more code on the next line.

```java title=Example.java

     def equalsign2(s: String) = {
       println("equalsign2: " + s)
     }
```

The following Trailing commas, periods, and operators indicate more code on the next line.

```java title=Example.java

      def commas(s1: String,
                s2: String) = Console.
       println("comma: " + s1 +
               ", " + s2)
```

- « Previous
