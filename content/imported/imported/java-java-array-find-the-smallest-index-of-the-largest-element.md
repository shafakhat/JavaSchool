---
title: Java Array find the smallest index of the largest element
nav: Java Array find the smalle...
description: Use a variable named indexOfMax to denote the index of the largest element.
section: Imported
order: 20001
source: http://www.java2s.com/ref/java/java-array-find-the-smallest-index-of-the-largest-element.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Use a variable named max to store the largest element

Use a variable named indexOfMax to denote the index of the largest element.

Initially max is array[0], and indexOfMax is 0.

Compare each element in array with max, and update max and indexOfMax if the element is greater than max.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = newint[5];

    for (int i = 0; i < array.length; i++) {
      array[i] = (int)(Math.random() * 100);
    } /*fromwww.java2s.com*/for (int i = 0; i < array.length; i++) {
      System.out.print(array[i] + " ");
    }

    double max = array[0];
    int indexOfMax = 0;
    for (int i = 1; i < array.length; i++) {
       if (array[i] > max) {
        max = array[i];
        indexOfMax = i;
      }
    }

    System.out.println(max+" @ "+ indexOfMax);
  }
}
```

PreviousNext

## Related

- Java Array display arrays
- Java Array find array element above average
- Java Array find the largest element
- Java Array for each loop through first 5 element
- Java Array initialize arrays with input values
