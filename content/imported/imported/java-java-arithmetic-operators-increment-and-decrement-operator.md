---
title: Java Arithmetic Operators Increment and Decrement Operator
nav: Java Arithmetic Operators ...
description: The ++ and the -- are Java's increment and decrement operators.
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20210102113207/http://www.java2s.com/ref/java/java-arithmetic-operators-increment-and-decrement-operator.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

The ++ and the -- are Java's increment and decrement operators.

The increment operator increases its operand by one.

The decrement operator decreases its operand by one.

For example, this statement:

```java title=Example.java

x = x + 1;
```

can be rewritten like this by use of the increment operator:

```java title=Example.java

x++;
```

This statement:

```java title=Example.java

x = x - 1;
```

is equivalent to

```java title=Example.java

x--;
```

Java Increment and Decrement Operator can appear in postfix form and prefix form.

In postfix form, they follow the operand.

In prefix form, they precede the operand.

In the prefix form, the operand is incremented or decremented before the value is obtained for use in the expression.

In postfix form, the previous value is obtained for use in the expression, and then the operand is modified.

For example:

```java title=Example.java

x = 42;
y = ++x;
```

In the code above, y is set to 43, because the increment occurs before x is assigned to y.

Thus, the line y=++x; is the equivalent of these two statements:

```java title=Example.java

x = x + 1;
y = x;
```

However, when written like this,

```java title=Example.java

x = 42;
y = x++;
```

The value of x is obtained before the increment operator is executed, so the value of y is 42.

In both cases x is set to 43.

Here, the line y=x++; is the equivalent of these two statements:

```java title=Example.java

y = x;
x = x + 1;
```

The following program demonstrates the increment operator.

```java title=Example.java
// Demonstrate ++ and --.publicclass Main {
  publicstaticvoid main(String args[]) {
    int a = 1;/*www.java2s.com*/int b = 2;
    int c;
    int d;

    c = ++b;
    d = a++;
    c++;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operators Modulus Operator calculate Greatest Common Divisor
- Java Arithmetic Operators Compound Assignment Operators
- Java Arithmetic Operators Compound Assignment Operators Question 1
- Java Bitwise Operators
- Java Bitwise Operators Logical Operators
