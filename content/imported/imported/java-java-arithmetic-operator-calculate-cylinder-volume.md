---
title: Java Arithmetic Operator calculate cylinder volume
nav: Java Arithmetic Operator c...
description: We would like to write a program that reads in the radius and length of a cylinder.
section: Imported - java2s Archive
order: 1059
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-cylinder-volume.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that reads in the radius and length of a cylinder.

Compute the area and volume using the following formulas:

```java title=Example.java

area = radius * radius * p
volume = area * length
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter the radius and length of a cylinder: ");
    double radius = input.nextDouble();
    double length = input.nextDouble();

    //your code hereSystem.out.println("The area is " + area);
    System.out.println("The volume is " + volume);
  }//fromwww.java2s.comprivatestaticdouble areaOfCylinder(double radius) {
    return radius * radius * Math.PI;
  }

  privatestaticdouble volumeOfCylinder(double area, double length) {
    return area * length;
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter the radius and length of a cylinder: ");
    double radius = input.nextDouble();
    double length = input.nextDouble();

    double area = areaOfCylinder(radius);
    double volume = volumeOfCylinder(area, length);

    System.out.println("The area is " + area);
    System.out.println("The volume is " + volume);
  }

  privatestaticdouble areaOfCylinder(double radius) {
    return radius * radius * Math.PI;
  }

  privatestaticdouble volumeOfCylinder(double area, double length) {
    return area * length;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate circle area with console input
- Java Arithmetic Operator calculate compound value
- Java Arithmetic Operator calculate distance of two points
- Java Arithmetic Operator calculate floating point value
