---
title: Java Array multidimensional Arrays sum elements by column
nav: Java Array multidimensiona...
description: For each column, use a variable named total to store its sum.
section: Imported
order: 20002
source: http://www.java2s.com/ref/java/java-array-multidimensional-arrays-sum-elements-by-column.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to sum elements by column.

For each column, use a variable named total to store its sum.

Add each element in the column to total using a loop.

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) {
    int[][] matrix = { { 1, 2 }, { 3, 4 }, { 5, 6 } };

    System.out.println(Arrays.deepToString(matrix));
    //your code here
  }/*fromwww.java2s.com*/
}
```

```java title=Example.java
import java.util.Arrays;

publicclass Main {

  publicstaticvoid main(String[] args) {
    int[][] matrix = { { 1, 2 }, { 3, 4 }, { 5, 6 } };

    System.out.println(Arrays.deepToString(matrix));
    for (int column = 0; column < matrix[0].length; column++) {
      int total = 0;
      for (int row = 0; row < matrix.length; row++)
        total += matrix[row][column];
      System.out.println("Sum for column " + column + " is " + total);
    }
  }
}
```

PreviousNext

## Related

- Java Array multidimensional Arrays print array
- Java Array multidimensional Arrays shuffle
- Java Array multidimensional Arrays sum all elements
- Java Array multidimensional Arrays for each loop iterate
- Java Array multidimensional Arrays find the closest pair of points
