---
title: Java Arithmetic Operators Modulus Operator find the factors of an integer
nav: Java Arithmetic Operators ...
description: For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20210102113206/http://www.java2s.com/ref/java/java-arithmetic-operators-modulus-operator-find-the-factors-of-an-inte.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that reads an integer.

Display all its smallest factors in increasing order.

For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter an integer: ");
    int n = input.nextInt();

    int i = 2;//fromwww.java2s.com//your code hereSystem.out.println();
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter an integer: ");
    int n = input.nextInt();

    int i = 2;
    while (n != 1) {
      if (n % i == 0) {
        System.out.print(i + " ");
        n /= i;
      } else {
        i++;
      }
    }
    System.out.println();
  }

}
```

PreviousNext

## Related

- Java switch two int values without using the third variable
- Java Arithmetic Operators
- Java Arithmetic Operators Modulus Operator
- Java Arithmetic Operators Modulus Operator start new line every 10 elements
- Java Arithmetic Operators Modulus Operator find three digit palindrome number
