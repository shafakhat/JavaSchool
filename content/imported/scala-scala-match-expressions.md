---
title: Scala Tutorial - Scala Match Expressions
nav: Scala Tutorial - Scala Mat...
description: We can use it to construct complex tests in very little code.
section: Imported - java2s Archive
order: 50096
source: https://www.java2s.com/Tutorials/Java/Scala/0270__Scala_Match_Expressions.html
---
Scala's match expressions are used for pattern matching.

We can use it to construct complex tests in very little code.

Pattern matching is like Java's switch statement, but we can test against almost anything, and we can assign the matched value to variables.

Scala pattern matching is an expression, so it results in a value that may be assigned or returned.

The most basic pattern matching is like Java's switch, except there is no break in each case as the cases do not fall through to each other.

## Example

The following code matches the number against a constant, but with a default.

```java title=Example.java
44 match {
    case 44 => true// if we match 44,the result is true
    case _ => false// otherwise the result isfalse
}
```

The following code shows how to match against a String.

```java title=Example.java
"CSS" match {
    case "CSS"=> 45 // the result is 45 if we match "CSS"
    case "Elwood" => 77
    case _ => 0
}
```

- « Previous
