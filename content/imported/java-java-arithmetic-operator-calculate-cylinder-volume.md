---
title: Java Arithmetic Operator calculate cylinder volume
nav: Java Arithmetic Operator c...
description: We would like to write a program that reads in the radius and length of a cylinder.
section: Imported - java2s Archive
order: 1059
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-cylinder-volume.html
---
## Question

We would like to write a program that reads in the radius and length of a cylinder.

Compute the area and volume using the following formulas:

```java title=Example.java
area = radius * radius * p
volume = area * length
java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter the radius and length of a cylinder: ");
    double radius = input.nextDouble();
    double length = input.nextDouble();
    //your code hereSystem.out.println("The area is " + area);
    System.out.println("The volume is " + volume);
  }privatestaticdouble areaOfCylinder(double radius) {
    return radius * radius * Math.PI;
  }
  privatestaticdouble volumeOfCylinder(double area, double length) {
    return area * length;
  }
}
java title=Example.java
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
