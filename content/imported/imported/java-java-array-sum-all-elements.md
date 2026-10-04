---
title: Java Array sum all elements
nav: Java Array sum all elements
description: Add each element in the array to total using a loop like this:
section: Imported
order: 20011
source: http://www.java2s.com/ref/java/java-array-sum-all-elements.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Use a variable named total to store the sum.

Initially total is?0.

Add each element in the array to total using a loop like this:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = newint[5];

    for (int i = 0; i < array.length; i++) {
      array[i] = (int)(Math.random() * 100);
    } //fromwww.java2s.comfor (int i = 0; i < array.length; i++) {
      System.out.print(array[i] + " ");
    }

    double total = 0;
    for (int i = 0; i < array.length; i++) {
      total += array[i];
    }

    System.out.println(total);
  }
}
```

PreviousNext

## Related

- Java Array random shuffle
- Java Array select random cards from deck
- Java Array shift elements
- Java Array Common Error
- Java Array multidimensional Arrays
