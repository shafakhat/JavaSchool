---
title: Java Arithmetic Operators
nav: Java Arithmetic Operators
description: Java arithmetic operators are used in mathematical expressions in the same way that they are used in math.
section: Imported - java2s Archive
order: 1095
source: https://web.archive.org/web/20210102113206/http://www.java2s.com/ref/java/java-arithmetic-operators.html
---
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
