---
title: Java Array multidimensional Arrays pass to methods
nav: Java Array multidimensiona...
description: /*fromwww.java2s.com*/// Display resultSystem.out.println("\nSum of all elements is " + sum(m));
section: Imported
order: 20006
source: http://www.java2s.com/ref/java/java-array-multidimensional-arrays-pass-to-methods.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Array multidimensional Arrays pass to methods

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    int[][] m = newint[3][4];
    for (int i = 0; i < m.length; i++)
      for (int j = 0; j < m[i].length; j++)
        m[i][j] = (int)(Math.random()*10);

    System.out.println(Arrays.deepToString(m));
    /*fromwww.java2s.com*/// Display resultSystem.out.println("\nSum of all elements is " + sum(m));
  }

  publicstaticint sum(int[][] m) {
    int total = 0;
    for (int row = 0; row < m.length; row++) {
      for (int column = 0; column < m[row].length; column++) {
        total += m[row][column];
      }
    }

    return total;
  }
}
```

PreviousNext

## Related

- Java Array multidimensional Arrays sum elements by column
- Java Array multidimensional Arrays for each loop iterate
- Java Array multidimensional Arrays find the closest pair of points
- Java Array multidimensional Arrays reference element
- Java Array search unsorted array for a value using for each loop
