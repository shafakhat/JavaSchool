---
title: Java Array multidimensional Arrays for each loop iterate
nav: Java Array multidimensiona...
description: A two-dimensional Java array is an array of one-dimensional arrays.
section: Imported
order: 20008
source: http://www.java2s.com/ref/java/java-array-multidimensional-arrays-for-each-loop-iterate.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

We can use the for-each loop on multidimensional arrays.

Java multidimensional arrays is arrays of arrays.

A two-dimensional Java array is an array of one-dimensional arrays.

```java title=Example.java
// Use for-each style for on a two-dimensional array.  publicclass Main {
  publicstaticvoid main(String args[]) {
    int sum = 0;
    int nums[][] = newint[3][5];

    // give nums some values  for(int i = 0; i < 3; i++)
      for(int j=0; j < 5; j++)
        nums[i][j] = (i+1)*(j+1);  //fromwww.java2s.com// use for-each for to display and sum the values  for(int[] x : nums) {
      for(int y : x) {
        System.out.println("Value is: " + y);
        sum += y;
      }
    }
    System.out.println("Summation: " + sum);
  }
}
```

PreviousNext

## Related

- Java Array multidimensional Arrays shuffle
- Java Array multidimensional Arrays sum all elements
- Java Array multidimensional Arrays sum elements by column
- Java Array multidimensional Arrays find the closest pair of points
- Java Array multidimensional Arrays pass to methods
