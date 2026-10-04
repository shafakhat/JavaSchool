---
title: Java Arithmetic Operator divisible by 3
nav: Java Arithmetic Operator d...
description: Imported from the java2s.com archive: Java Arithmetic Operator divisible by 3
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20210102113217/http://www.java2s.com/ref/java/java-arithmetic-operator-divisible-by-3.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to check if a number is divisible by 3.

Read the integer from console.

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] args) {
    /*fromwww.java2s.com*/Scanner input = newScanner(System.in);
    int x;

    System.out.print("Enter integer you wish to check: ");
    x = input.nextInt();

    //your code here

    input.close();
  }

}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] args) {

    Scanner input = newScanner(System.in);
    int x;

    System.out.print("Enter integer you wish to check: ");
    x = input.nextInt();

    if (x % 3 == 0)
      System.out.println("Yep, it's divisible by 3!");
    if (x % 3 != 0)
      System.out.println("Nope, it's not divisible by 3!");

    input.close();
  }

}
```

PreviousNext

## Related

- Java Arithmetic Operator convert feet into meters
- Java Arithmetic Operator convert pounds into kilograms
- Java Arithmetic Operator divide two integer
- Java Arithmetic Operator find the number of years
- Java Arithmetic Operator increment and decrement result 1
