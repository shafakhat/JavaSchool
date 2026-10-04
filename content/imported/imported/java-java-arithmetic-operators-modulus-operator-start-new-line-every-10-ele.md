---
title: Java Arithmetic Operators Modulus Operator start new line every 10 elements
nav: Java Arithmetic Operators ...
description: Java Arithmetic Operators Modulus Operator start new line every 10 elements
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20210102113206/http://www.java2s.com/ref/java/java-arithmetic-operators-modulus-operator-start-new-line-every-10-ele.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Arithmetic Operators Modulus Operator start new line every 10 elements

```java title=Example.java
import java.util.Random;

publicclass Main {

  publicstaticvoid main(String... args) {

    Random rand = newRandom();
    int[] a = newint[100];
    for (int i = 0; i < 100; i++) {
      a[i] = rand.nextInt(100);//fromwww.java2s.comSystem.out.print(a[i] + ", ");
      if ((i + 1) % 10 == 0) {
        System.out.println();
      }
    }
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operators
- Java Arithmetic Operators Modulus Operator
- Java Arithmetic Operators Modulus Operator find the factors of an integer
- Java Arithmetic Operators Modulus Operator find three digit palindrome number
- Java Arithmetic Operators Modulus Operator calculate Greatest Common Divisor
