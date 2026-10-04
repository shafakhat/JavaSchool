---
title: Java Arithmetic Operator calculate area of a triangle
nav: Java Arithmetic Operator c...
description: Prompt the user to enter three points (x1, y1), (x2, y2), (x3,y3) of a triangle,
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20210102113213/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-area-of-a-triangle.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to calculate area of a triangle.

Prompt the user to enter three points (x1, y1), (x2, y2), (x3,y3) of a triangle,

Display its area.

The formula for computing the area of a triangle is

```java title=Example.java

s  =  (side1  + side2  +  side3)/2;
area  =  2s(s  -  side1)(s  -  side2)(s  -  side3)
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);
    System.out.print("Enter three points for a triangle: ");

    // triangle pointsdouble x1 = input.nextDouble();
    double y1 = input.nextDouble();
    double x2 = input.nextDouble();
    double y2 = input.nextDouble();
    double x3 = input.nextDouble();
    double y3 = input.nextDouble();

    //your code//www.java2s.comSystem.out.println("The area of the triangle is " + area);
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);
    System.out.print("Enter three points for a triangle: ");

    // triangle pointsdouble x1 = input.nextDouble();
    double y1 = input.nextDouble();
    double x2 = input.nextDouble();
    double y2 = input.nextDouble();
    double x3 = input.nextDouble();
    double y3 = input.nextDouble();

    // gettings sides of triangledouble side1 = Math.pow((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2), 0.5);
    double side2 = Math.pow((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3), 0.5);
    double side3 = Math.pow((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2), 0.5);

    double s = (side1 + side2 + side3) / 2.0;
    double area = Math.pow(s * (s - side1) * (s - side2) * (s - side3), 0.5);

    System.out.println("The area of the triangle is " + area);
  }
}
```

Use method

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter three points for a triangle: ");
    double x1 = input.nextDouble();
    double y1 = input.nextDouble();
    double x2 = input.nextDouble();
    double y2 = input.nextDouble();
    double x3 = input.nextDouble();
    double y3 = input.nextDouble();

    double area = areaOfTriangle(x1, y1, x2, y2, x3, y3);

    System.out.println("The area of the triangle is " + area);
  }//www.java2s.comprivatestaticdouble areaOfTriangle(double x1, double y1, double x2,
    double y2, double x3, double y3) {
    double s1 = distance(x1, y1, x2, y2);
    double s2 = distance(x2, y2, x3, y3);
    double s3 = distance(x3, y3, x1, y1);
    double s = (s1 + s2 + s3) / 2.0;
    returnMath.sqrt(s * (s - s1) * (s - s2) * (s - s3));
  }

  privatestaticdouble distance(double x1, double y1, double x2, double y2) {
    returnMath.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator Body Mass Index Calculator(BMI)
- Java Arithmetic Operator calculate area and perimeter of a circle
- Java Arithmetic Operator calculate area and perimeter of a rectangle
- Java Arithmetic Operator calculate average speed in kilometers
- Java Arithmetic Operator calculate average speed in miles
