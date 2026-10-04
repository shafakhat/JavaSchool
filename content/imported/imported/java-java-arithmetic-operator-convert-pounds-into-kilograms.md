---
title: Java Arithmetic Operator convert pounds into kilograms
nav: Java Arithmetic Operator c...
description: We would like to write a program that converts pounds into kilograms.
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-convert-pounds-into-kilograms.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that converts pounds into kilograms.

The program prompts the user to enter a number in pounds, converts it to kilograms.

Display the result.

One pound is 0.454 kilograms.

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);
    System.out.print("Enter a number in pounds: ");

    //your code/*fromwww.java2s.com*/
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);
    System.out.print("Enter a number in pounds: ");

    double pounds = input.nextDouble();
    double kilograms = pounds * 0.454;

    System.out.println(pounds + " pounds is " + kilograms + " kilograms.");
  }
}
```

## Note

Define a method to do the conversion.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a number in pounds: ");
    double pounds = input.nextDouble();

    double kilograms = poundsToKilograms(pounds);

    System.out.println(pounds + " pounds is " + kilograms + " kilograms");
  }//www.java2s.comprivatestaticdouble poundsToKilograms(double pounds) {
    return pounds * 0.454;
  }
}
```

Create a constant for the conversion.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);   // Create new Scanner objectfinaldouble KILOGRAMS_PER_POUND = 0.454; // Create constant value// Prompt user to enter the number of poundsSystem.out.print("Enter a number in pounds: ");
    double pounds = input.nextDouble();

    // Convert pounds into kilogramsdouble kilograms = pounds * KILOGRAMS_PER_POUND;

    // Display the resultsSystem.out.println(pounds + " pounds is " + kilograms + " kilograms");
  }/*www.java2s.com*/
}
```

PreviousNext

## Related

- Java Arithmetic Operator compute expressions
- Java Arithmetic Operator convert celsius to fahrenheit
- Java Arithmetic Operator convert feet into meters
- Java Arithmetic Operator divide two integer
- Java Arithmetic Operator divisible by 3
