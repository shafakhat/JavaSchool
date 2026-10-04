---
title: Java Array multidimensional Arrays find the closest pair of points
nav: Java Array multidimensiona...
description: We would like to find the closest pair of points using multidimensional array.
section: Imported
order: 20007
source: http://www.java2s.com/ref/java/java-array-multidimensional-arrays-find-the-closest-pair-of-points.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to find the closest pair of points using multidimensional array.

Given a set of points, the closest-pair problem is to find the two points that are nearest to each other.

We can compute the distances between all pairs of points and find the one with the minimum distance.

```java title=Example.java
 AnswerCode:

 publicclass Main {
   publicstaticvoid main(String[] args) {
     int numberOfPoints = 5;

     // Create an array to store pointsdouble[][] points = newdouble[numberOfPoints][2];
     for (int i = 0; i < points.length; i++) {
       points[i][0] = Math.random()*(Math.random()*20);
       points[i][1] = Math.random()*(Math.random()*300);
     }/*www.java2s.com*///your code
   }

   /** Compute the distance between two points (x1, y1) and (x2, y2) */publicstaticdouble distance(double x1, double y1, double x2, double y2) {
     returnMath.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
   }
 }
```

PreviousNext

## Related

- Java Array multidimensional Arrays sum all elements
- Java Array multidimensional Arrays sum elements by column
- Java Array multidimensional Arrays for each loop iterate
- Java Array multidimensional Arrays pass to methods
- Java Array multidimensional Arrays reference element
