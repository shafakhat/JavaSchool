---
title: Java Arithmetic Operator convert feet into meters
nav: Java Arithmetic Operator c...
description: We would like to write a program that reads a number in feet.
section: Imported - java2s Archive
order: 1069
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-convert-feet-into-meters.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that reads a number in feet.

Convert it to meters, and displays the result.

One foot is 0.305 meter. Here is a sample run:

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);

    //your code here

  }/*fromwww.java2s.com*/
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);

    System.out.print("Enter a value for feet: ");
    double feet = input.nextDouble();
    double meters = feet * 0.305;
    System.out.println(feet + " feet is " + meters + " meters");

  }
}
```

## Note

To define a method

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a value for feet: ");
    double feet = input.nextDouble();

    double meters = feetToMeters(feet);

    System.out.println(feet + " feet is " + meters + " meters");
  }//fromwww.java2s.comprivatestaticdouble feetToMeters(double feet) {
    return feet * 0.305;
  }
}
```

Define a constant for converting.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);

    // Create constant valuefinaldouble METERS_PER_FOOT = 0.305;

    // Prompt user to enter a number in feetSystem.out.print("Enter a value for feet: ");
    double feet = input.nextDouble();

    // Convert feet into metersdouble meters = feet * METERS_PER_FOOT;

    // Display resultsSystem.out.println(feet + " feet is " + meters + " meters");
  }//www.java2s.com
}
```

PreviousNext

## Related

- Java Arithmetic Operator compound operator result
- Java Arithmetic Operator compute expressions
- Java Arithmetic Operator convert celsius to fahrenheit
- Java Arithmetic Operator convert pounds into kilograms
- Java Arithmetic Operator divide two integer
