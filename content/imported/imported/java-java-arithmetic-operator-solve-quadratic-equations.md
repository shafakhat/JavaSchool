---
title: Java Arithmetic Operator solve quadratic equations
nav: Java Arithmetic Operator s...
description: ax2 + bx + c = 0 b2 - 4ac is called the discriminant of the quadratic equation.
section: Imported - java2s Archive
order: 1088
source: https://web.archive.org/web/20210102113220/http://www.java2s.com/ref/java/java-arithmetic-operator-solve-quadratic-equations.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to solve quadratic equations using Java.

ax2 + bx + c = 0 b2 - 4ac is called the discriminant of the quadratic equation.

- If it is positive, the equation has two real roots.
- If it is zero, the equation has one root.
- If it is negative, the equation has no real roots.

Write a program that prompts the user to enter values for a, b, and c.

Display the result based on the discriminant.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);

    // Prompt the user to enter values for a, b and c.System.out.print("Enter a, b, c: ");
    double a = input.nextDouble();
    double b = input.nextDouble();
    double c = input.nextDouble();

    double discriminant = Math.pow(b, 2) - 4 * a * c;

    System.out.print("The equation has ");
    if (discriminant > 0) {
      double root1 = (-b + Math.pow(discriminant, 0.5)) / (2 * a);
      double root2 = (-b - Math.pow(discriminant, 0.5)) / (2 * a);
      System.out.println("two roots " + root1 + " and " + root2);
    } elseif (discriminant == 0) {
      double root1 = (-b + Math.pow(discriminant, 0.5)) / (2 * a);
      System.out.println("one root " + root1);
    } elseSystem.out.println("no real roots");
  }
}
```

To define method for the calculation:

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a, b, c: ");
    double a = input.nextDouble();
    double b = input.nextDouble();
    double c = input.nextDouble();

    displayRoots(a, b, c);/*fromwww.java2s.com*/
  }

  privatestaticvoid displayRoots(double a, double b, double c) {
    double d = discriminant(a, b, c);
    double r1 = 0.0;
    double r2 = 0.0;
    StringBuilder output = newStringBuilder("The equation has ");

    if (d > 0) {
      r1 = calculateRoot(a, b, d, true);
      r2 = calculateRoot(a, b, d, false);
      output.append("two roots " + r1 + " and " + r2);
    } elseif (d < 0) {
      output.append("no real roots");
    } else {
      r1 = calculateRoot(a, b, d, true);
      output.append("one root " + r1);
    }

    System.out.println(output);
  }

  privatestaticdouble calculateRoot(double a, double b, double disc,
    boolean isR1) {
    double root;
    if (isR1) {
      root = (-b + Math.sqrt(disc)) / (2 * a);
    } else {
      root = (-b - Math.sqrt(disc)) / (2 * a);
    }
    return root;
  }

  privatestaticdouble discriminant(double a, double b, double c) {
    return (b * b) - (4 * a * c);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator remainder operator
- Java Arithmetic Operator separate the Digits in an Integer
- Java Arithmetic Operator solve 2 by 2 linear equations
- Java Arithmetic Operator sum a list of numbers
- Java Arithmetic Operator sum the digits in an integer
