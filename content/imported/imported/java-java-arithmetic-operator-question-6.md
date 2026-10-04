---
title: Java Arithmetic Operator Question 6
nav: Java Arithmetic Operator Q...
description: The assignment operator is performed last after all the other operators in the expression are evaluated.
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20210102113218/http://www.java2s.com/ref/java/java-arithmetic-operator-question-6.html
---
## Question

What is the output of the following code?

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    double x = 10;
    x /= 10 + 5 * 2;
    System.out.println("x: " + x);
  }
}
```

```java title=Example.java
x: 0.5
```

## Note

Java Assignment Operators:

| Operator | Name | Example | Equivalent |
|---|---|---|---|
| += | Addition assignment | i += 8 | i = i + 8 |
| -= | Subtraction assignment | i -= 8 | i = i - 8 |
| *= | Multiplication assignment | i *= 8 | i = i * 8 |
| /= | Division assignment | i /= 8 | i = i / 8 |
| %= | Remainder assignment | i %= 8 | i = i % 8 |

The assignment operator is performed last after all the other operators in the expression are evaluated.

For example,

```java title=Example.java

x /= 10 + 5 * 2;
is
x = x / (10 + 5 * 2);
```

PreviousNext

## Related

- Java Arithmetic Operator Question 3
- Java Arithmetic Operator Question 4
- Java Arithmetic Operator Question 5
- Java Arithmetic Operator Question 7
- Java Arithmetic Operator Question 8
