---
title: Java Arithmetic Operator remainder operator
nav: Java Arithmetic Operator r...
description: We would like to find out the changes for give numbers of money.
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20210102113219/http://www.java2s.com/ref/java/java-arithmetic-operator-remainder-operator.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to find out the changes for give numbers of money.

The total money we have is 248 cents.

The code should output the quarters, dimes, nickels, cents it include.

```java title=Example.java
publicclass Main {

  publicstaticvoid main(String args[]) {
    int total = 248;

    //your code here
  }
}
```

```java title=Example.java
publicclass Main {

  publicstaticvoid main(String args[]) {
    int total = 248;
    int quarters = total / 25;
    int whatsLeft = total % 25;

    int dimes = whatsLeft / 10;
    whatsLeft = whatsLeft % 10;

    int nickels = whatsLeft / 5;
    whatsLeft = whatsLeft % 5;

    int cents = whatsLeft;

    System.out.println("From " + total + " cents you get");
    System.out.println(quarters + " quarters");
    System.out.println(dimes + " dimes");
    System.out.println(nickels + " nickels");
    System.out.println(cents + " cents");
  }
}
```

The symbol for the remainder operator is the percent sign (%).

PreviousNext

## Related

- Java Arithmetic Operator Question 9
- Java Arithmetic Operator Question 10
- Java Arithmetic Operator Question 11
- Java Arithmetic Operator separate the Digits in an Integer
- Java Arithmetic Operator solve 2 by 2 linear equations
