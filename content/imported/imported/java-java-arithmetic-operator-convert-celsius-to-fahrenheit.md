---
title: Java Arithmetic Operator convert celsius to fahrenheit
nav: Java Arithmetic Operator c...
description: We would like to convert celsius to fahrenheit using double type:
section: Imported - java2s Archive
order: 1068
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-convert-celsius-to-fahrenheit.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to convert celsius to fahrenheit using double type:

Write a program that reads a Celsius degree in a double value from the console.

Convert it to Fahrenheit and displays the result.

The formula for the conversion is as follows:

```java title=Example.java

fahrenheit = (9 / 5) * celsius + 32
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);

    System.out.print("Enter a degree in Celsius: ");
    double celsius = input.nextDouble();

    //your code here/*fromwww.java2s.com*/System.out.println(celsius + " degree Celsius is equal to " + fahrenheit + " in Fahrenheit");
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);

    System.out.print("Enter a degree in Celsius: ");
    double celsius = input.nextDouble();

    double fahrenheit = (9.0 / 5.0) * celsius + 32.0;
    System.out.println(celsius + " degree Celsius is equal to " + fahrenheit + " in Fahrenheit");
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate/approximate PI
- Java Arithmetic Operator compound operator result
- Java Arithmetic Operator compute expressions
- Java Arithmetic Operator convert feet into meters
- Java Arithmetic Operator convert pounds into kilograms
