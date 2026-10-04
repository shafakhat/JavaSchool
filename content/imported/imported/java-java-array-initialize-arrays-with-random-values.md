---
title: Java Array initialize arrays with random values
nav: Java Array initialize arra...
description: The following loop initializes the array array with random values between 0.0 and 100.0, but less than 100.0.
section: Imported
order: 20000
source: http://www.java2s.com/ref/java/java-array-initialize-arrays-with-random-values.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

The following loop initializes the array array with random values between 0.0 and 100.0, but less than 100.0.

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = newint[5];

    for (int i = 0; i < array.length; i++) {
      array[i] = (int)(Math.random() * 100);
    } //www.java2s.comSystem.out.println(Arrays.toString(array));

  }
}
```

PreviousNext

## Related

- Java Array find the smallest index of the largest element
- Java Array for each loop through first 5 element
- Java Array initialize arrays with input values
- Java Array random shuffle
- Java Array select random cards from deck
