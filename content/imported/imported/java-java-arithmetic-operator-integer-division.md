---
title: Java Arithmetic Operator Integer division
nav: Java Arithmetic Operator I...
description: In Java, if you divide two integers, the result is an integer.
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20210102113218/http://www.java2s.com/ref/java/java-arithmetic-operator-integer-division.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following program

```java title=Example.java
publicclass Main {

   publicstaticvoid main(String args[]) {
      System.out.println(5 / 4);
      System.out.println(10 / 4);
   }
}
```

```java title=Example.java
1
2
```

## Note

In Java, if you divide two integers, the result is an integer.

The fractional part is truncated.

For example, 5 / 4 is 1 (not 1.25) and 10 / 4 is 2 (not 2.5).

To get an accurate result, make sure that one of the values involved in the division is a number with a decimal point.

For example, 5.0 / 4 is 1.25 and 10 / 4.0 is 2.5.

PreviousNext

## Related

- Java Arithmetic Operator find the number of years
- Java Arithmetic Operator increment and decrement result 1
- Java Arithmetic Operator increment and decrement result 2
- Java Arithmetic Operator Question 1
- Java Arithmetic Operator Question 2
