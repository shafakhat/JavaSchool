---
title: Java Array find array element above average
nav: Java Array find array elem...
description: The problem is to write a program that finds the number of items above the average of all items.
section: Imported - java2s Archive
order: 1107
source: https://web.archive.org/web/20210102113249/http://www.java2s.com/ref/java/java-array-find-array-element-above-average.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

The problem is to write a program that finds the number of items above the average of all items.

- read 100 numbers
- get the average of these numbers
- find the number of the items greater than the average.
- let the user enter the number of input

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    java.util.Scanner input = new java.util.Scanner(System.in);
    System.out.print("Enter the number of items: ");
    int n = input.nextInt();
    double[] numbers = newdouble[n];
    double sum = 0;

    //your code here
  }/*fromwww.java2s.com*/
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    java.util.Scanner input = new java.util.Scanner(System.in);
    System.out.print("Enter the number of items: ");
    int n = input.nextInt();
    double[] numbers = newdouble[n];
    double sum = 0;

    System.out.print("Enter the numbers: ");
    for (int i = 0; i < n; i++) {
      numbers[i] = input.nextDouble();
      sum += numbers[i];
    }

    double average = sum / n;

    int count = 0; // The numbers of elements above averagefor (int i = 0; i < n; i++)
      if (numbers[i] > average)
        count++;

    System.out.println("Average is " + average);
    System.out.println("Number of elements above the average is "
      + count);
  }
}
```

PreviousNext

## Related

- Java Array as frequency counters
- Java Array count occurrences of letter in char array
- Java Array display arrays
- Java Array find the largest element
- Java Array find the smallest index of the largest element
