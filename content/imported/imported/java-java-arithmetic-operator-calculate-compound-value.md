---
title: Java Arithmetic Operator calculate compound value
nav: Java Arithmetic Operator c...
description: Suppose you save $100 each month into a savings account with the annual interest rate 5%.
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-compound-value.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to calculate compound value.

Suppose you save $100 each month into a savings account with the annual interest rate 5%.

Thus, the monthly interest rate is 0.05/12 = 0.00417.

After the first month, the value in the account becomes 100 * (1 + 0.00417) = 100.417

After the second month, the value in the account becomes (100 + 100.417) * (1 + 0.00417) = 201.252

After the third month, the value in the account becomes (100 + 201.252) * (1 + 0.00417) = 302.507

Write a program that prompts the user to enter a monthly saving amount.

Display the account value after the sixth month.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in); // Create a new Scanner object.finaldouble MONTHLY_INTEREST_RATE = 0.00417; // Initialize constant value// Prompt the user to enter a montly saving amountSystem.out.print("Enter the monthly saving amount: ");
    double savingAmount = input.nextDouble();

    //your code here// Display resultSystem.out.println("After the sixth month, the account value is " + total);
  }/*fromwww.java2s.com*/
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in); // Create a new Scanner object.finaldouble MONTHLY_INTEREST_RATE = 0.00417; // Initialize constant value// Prompt the user to enter a montly saving amountSystem.out.print("Enter the monthly saving amount: ");
    double savingAmount = input.nextDouble();

    // Compute first month account valuedouble total = savingAmount * (1 + MONTHLY_INTEREST_RATE);
    // Compute second month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute third month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute forth month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute fifth month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute sixth month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);

    // Display resultSystem.out.println("After the sixth month, the account value is " + total);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate average speed in miles
- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate circle area with console input
- Java Arithmetic Operator calculate cylinder volume
- Java Arithmetic Operator calculate distance of two points
