---
title: Java Arithmetic Operator Question 6
nav: Java Arithmetic Operator Q...
description: The assignment operator is performed last after all the other operators in the expression are evaluated.
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20210102113218/http://www.java2s.com/ref/java/java-arithmetic-operator-question-6.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

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
