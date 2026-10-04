---
title: Java Arithmetic Operator calculate circle area with console input
nav: Java Arithmetic Operator c...
description: import java.util.Scanner; // Scanner is in the java.util packagepublicclass Main {
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-circle-area-with-console-input.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to calculate circle area with console input.

Code structure you can use:

```java title=Example.java
import java.util.Scanner; // Scanner is in the java.util packagepublicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);
    /*fromwww.java2s.com*/// Prompt the user to enter a radiusSystem.out.print("Enter a number for radius: ");
    double radius = input.nextDouble();

    //your code here
  }
}
```

```java title=Example.java
import java.util.Scanner; // Scanner is in the java.util packagepublicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);

    // Prompt the user to enter a radiusSystem.out.print("Enter a number for radius: ");
    double radius = input.nextDouble();

    // Compute areadouble area = radius * radius * 3.14159;

    // Display resultSystem.out.println("The area for the circle of radius " +
      radius + " is " + area);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate average speed in kilometers
- Java Arithmetic Operator calculate average speed in miles
- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate compound value
- Java Arithmetic Operator calculate cylinder volume
