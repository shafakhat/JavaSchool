---
title: Java Arithmetic Operator sum the digits in an integer
nav: Java Arithmetic Operator s...
description: We would like to write a program that reads an integer between 0 and 1000.
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20210102113220/http://www.java2s.com/ref/java/java-arithmetic-operator-sum-the-digits-in-an-integer.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that reads an integer between 0 and 1000.

Add all the digits in the integer.

For example, if an integer is 932, the sum of all its digits is 14.

## Hint

Use the % operator to extract digits

Use the / operator to remove the extracted digit.

For instance, 932 % 10 = 2 and 932 / 10 = 93.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);   // Create new Scanner object// Prompt the user to enter a number between 0 and 1000.System.out.print("Enter a number between 0 and 1000: ");
    int number = input.nextInt();

    //your code here// Display resultsSystem.out.println("The sum of the digits is " + sum);
  }/*www.java2s.com*/
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);   // Create new Scanner object// Prompt the user to enter a number between 0 and 1000.System.out.print("Enter a number between 0 and 1000: ");
    int number = input.nextInt();

    // Compute the sum of the digits in the integer.int lessThan10 = number % 10;   // Extract the digit less than 10
    number /= 10;             // Remove the extracted digitint tens = number % 10;       // Extract the digit between 10 to 99
    number /= 10;             // Remove the extracted digitint hundreds = number % 10;   // Extract the digit between 100 to 999
    number /= 10;             // Remove the extracted digitint sum = hundreds + tens + lessThan10;

    // Display resultsSystem.out.println("The sum of the digits is " + sum);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator solve 2 by 2 linear equations
- Java Arithmetic Operator solve quadratic equations
- Java Arithmetic Operator sum a list of numbers
- Java Boolean Logical Operators truth table
- Java if statement
