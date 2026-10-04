---
title: Java Arithmetic Operator calculate area and perimeter of a circle
nav: Java Arithmetic Operator c...
description: We would like to write a program that displays the area and perimeter of a circle that has a radius of 5.5.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20210102113213/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-area-and-perimeter-of-a-circle.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that displays the area and perimeter of a circle that has a radius of 5.5.

The following formula you can use:

```java title=Example.java

perimeter   =  2  times  radius  times  pi
area  =  radius  times  radius  times  pi
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println("Perimeter = ");
    System.out.println(2 * 5.5 * 3.14159);
    System.out.println("Area = ");
    System.out.println(5.5 * 5.5 * 3.14159);
  }
}
```

## Note

We can also use the constant from Math class.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    double perimeter = perimeter(5.5);
    double area = area(5.5);
    System.out.println("perimeter: " + perimeter);
    System.out.println("area: " + area);
  }//fromwww.java2s.comprivatestaticdouble perimeter(double radius) {
    return 2 * radius * Math.PI;
  }

  privatestaticdouble area(double radius) {
    return radius * radius * Math.PI;
  }
}
```

PreviousNext

## Related

- Java Operator Precedence Question 1
- Java two's complement Integer in binary form
- Java Arithmetic Operator Body Mass Index Calculator(BMI)
- Java Arithmetic Operator calculate area and perimeter of a rectangle
- Java Arithmetic Operator calculate area of a triangle
