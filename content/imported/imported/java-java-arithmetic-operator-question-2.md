---
title: Java Arithmetic Operator Question 2
nav: Java Arithmetic Operator Q...
description: We would like to write an application that asks the user to enter two integers.
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20210102113218/http://www.java2s.com/ref/java/java-arithmetic-operator-question-2.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write an application that asks the user to enter two integers.

The get them from the user and print their sum, product, difference and quotient (division).

```java title=Example.java
import java.util.Scanner;

publicclass Main{
    publicstaticvoid main(String[] args){
        Scanner input = newScanner(System.in);

        //your code here
    }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main{
    publicstaticvoid main(String[] args){
        Scanner input = newScanner(System.in);

        int difference = 0;
        int quotient = 0;

        System.out.print("Enter 2 integers separated by a space: ");
        int x = input.nextInt();
        int y = input.nextInt();

        // sum
        printSolution("Sum", x + y);

        // product
        printSolution("Product", x * y);

        // difference
        printSolution("Difference", Math.abs(x - y));

        if(x != 0 && y != 0)
            printSolution("Quotient", y % x);
        else
            printSolution("Quotient error: Cannot divide by zero", 0);
    }
    privatestaticvoid printSolution(String message, int value){
        System.out.printf("%s = %d\n", message, value);
    }
}
```

Or you can do

```java title=Example.java
package chapter2;

import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] args) {
    /*www.java2s.com*/// Declaring variables needed for exerciseScanner input = newScanner(System.in);
    int x, y;
    int xsquare, ysquare;
    int sumsquare;
    int difsquare;

    // Prompting user for two integersSystem.out.print("Enter first integer: ");
    x = input.nextInt();
    System.out.println("Eter second integer: ");
    y = input.nextInt();

    // Performing calculations as described in exercise specification
    xsquare = x * x;
    ysquare = y * y;
    sumsquare = xsquare + ysquare;
    difsquare = xsquare - ysquare;

    // Displaying results to userSystem.out.printf("Square of x = %s, Square o y = %s.%nSum of squares = %s, Difference of squares = %s",
        xsquare, ysquare, sumsquare, difsquare);

    input.close();
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator increment and decrement result 2
- Java Arithmetic Operator Integer division
- Java Arithmetic Operator Question 1
- Java Arithmetic Operator Question 3
- Java Arithmetic Operator Question 4
