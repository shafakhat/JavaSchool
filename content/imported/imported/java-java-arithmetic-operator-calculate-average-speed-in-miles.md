---
title: Java Arithmetic Operator calculate average speed in miles
nav: Java Arithmetic Operator c...
description: Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-average-speed-in-miles.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.

We would like to write a program that displays the average speed in miles per hour.

1 mile is 1.6 kilometers.

Code structure you can use:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println();
  }
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println((14 / 45.30) / 1.6);
  }
}
```

## Note

To define method for the calculation:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println("mph: " + kphToMph(kilometersPerHour(14, 45.5)));
  }//fromwww.java2s.comprivatestaticdouble kilometersPerHour(double kilometers, double minutes) {
    return 60.0 * (kilometers / minutes);
  }

  privatestaticdouble kphToMph(double kph) {
    return kph / 1.6;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate area and perimeter of a rectangle
- Java Arithmetic Operator calculate area of a triangle
- Java Arithmetic Operator calculate average speed in kilometers
- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate circle area with console input
