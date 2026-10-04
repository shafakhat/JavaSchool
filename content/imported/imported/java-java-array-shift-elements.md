---
title: Java Array shift elements
nav: Java Array shift elements
description: The following code shifts the array elements one position to the left and filling the last element with the first element:
section: Imported
order: 20007
source: http://www.java2s.com/ref/java/java-array-shift-elements.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

The following code shifts the array elements one position to the left and filling the last element with the first element:

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    System.out.println(Arrays.toString(array));
    int temp = array[0]; // Retain the first element// Shift elements left arrayfor (int i = 1; i < array.length; i++) {
      array[i - 1] = array[i];/*fromwww.java2s.com*/
    }

    // Move the first element to fill in the last position
    array[array.length - 1] = temp;

    System.out.println(Arrays.toString(array));
  }
}
```

PreviousNext

## Related

- Java Array initialize arrays with random values
- Java Array random shuffle
- Java Array select random cards from deck
- Java Array sum all elements
- Java Array Common Error
