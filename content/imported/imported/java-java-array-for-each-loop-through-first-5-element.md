---
title: Java Array for each loop through first 5 element
nav: Java Array for each loop t...
description: We have an array with 10 element and we would like to use for each loop to display the first 5 element from that array.
section: Imported
order: 20000
source: http://www.java2s.com/ref/java/java-array-for-each-loop-through-first-5-element.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We have an array with 10 element and we would like to use for each loop to display the first 5 element from that array.

We also need to sum the value of first five elements.

Code structure to start with:

```java title=Example.java
// Use break with a for-each style for.   publicclass Main {
  publicstaticvoid main(String args[]) {
    int sum = 0;
    int nums[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    //Your code here//www.java2s.comSystem.out.println("Summation of first 5 elements: " + sum);
  }
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int sum = 0;
    int nums[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    // use for to display and sum the values  for(int x : nums) {
      System.out.println("Value is: " + x);
      sum += x;
      if(x == 5) break; // stop the loop when 5 is obtained
    }
    System.out.println("Summation of first 5 elements: " + sum);
  }
}
```

The for-each loop iterates the entire array.

We can use a break statement to terminate the looping.

PreviousNext

## Related

- Java Array find array element above average
- Java Array find the largest element
- Java Array find the smallest index of the largest element
- Java Array initialize arrays with input values
- Java Array initialize arrays with random values
