---
title: Java Array multidimensional Arrays reference element
nav: Java Array multidimensiona...
description: int[][][] array = { { { 1, 2 }, { 3, 4 } }, { { 5, 6 }, { 7, 8 } } };
section: Imported
order: 20001
source: http://www.java2s.com/ref/java/java-array-multidimensional-arrays-reference-element.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code?

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    int[][][] array = { { { 1, 2 }, { 3, 4 } }, { { 5, 6 }, { 7, 8 } } };
    System.out.println(array[0][0][0]);
    System.out.println(array[1][1][1]);
  }

}
```

```java title=Example.java
1
8
```

PreviousNext

## Related

- Java Array multidimensional Arrays for each loop iterate
- Java Array multidimensional Arrays find the closest pair of points
- Java Array multidimensional Arrays pass to methods
- Java Array search unsorted array for a value using for each loop
- Java array check if an array of primitive chars is empty or null.
