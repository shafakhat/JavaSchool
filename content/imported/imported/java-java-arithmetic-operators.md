---
title: Java Arithmetic Operators
nav: Java Arithmetic Operators
description: Java arithmetic operators are used in mathematical expressions in the same way that they are used in math.
section: Imported - java2s Archive
order: 1095
source: https://web.archive.org/web/20210102113206/http://www.java2s.com/ref/java/java-arithmetic-operators.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Java arithmetic operators are used in mathematical expressions in the same way that they are used in math.

The following table lists the arithmetic operators:

Operator  Result
---  ---
+  Addition and unary plus
-  Subtraction and unary minus
*  Multiplication
/  Division
%  Modulus
++  Increment
+=  Addition assignment
-=  Subtraction assignment
*=  Multiplication assignment
/=  Division assignment
%=  Modulus assignment
--  Decrement

The operands of the arithmetic operators must be of a numeric type.

You can use them on char types, since the char type in Java is a subset of int.

## Basic Arithmetic Operators

The basic arithmetic operations-addition, subtraction, multiplication, and division-behave the same as algebra.

The unary minus operator negates its single operand.

The unary plus operator returns the value of its operand.

When the division operator is used on an integer type, there will be no fractional component returned.

The following simple example program demonstrates the arithmetic operators.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    System.out.println("Integer Arithmetic");
    int a = 1 + 1;
    int b = a * 3;
    int c = b / 4;
    int d = c - a;
    int e = -d;/*www.java2s.com*/System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
    System.out.println("e = " + e);
  }
}
```

The following code illustrates the difference between floating-point division and integer division.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    // arithmetic using integersSystem.out.println("Integer Arithmetic");
    int a = 1 + 1;
    int b = a * 3;
    int c = b / 4;
    int d = c - a;
    int e = -d;//www.java2s.comSystem.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
    System.out.println("e = " + e);

    // arithmetic using doublesSystem.out.println("\nFloating Point Arithmetic");
    double da = 1 + 1;
    double db = da * 3;
    double dc = db / 4;
    double dd = dc - a;
    double de = -dd;
    System.out.println("da = " + da);
    System.out.println("db = " + db);
    System.out.println("dc = " + dc);
    System.out.println("dd = " + dd);
    System.out.println("de = " + de);
  }
}
```

PreviousNext

## Related

- Java type conversion and casting Question 3
- Java type promotion rules
- Java switch two int values without using the third variable
- Java Arithmetic Operators Modulus Operator
- Java Arithmetic Operators Modulus Operator find the factors of an integer
