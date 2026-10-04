---
title: Java array find the max and min value via Collections.min/max
nav: Java array find the max an...
description: Java array find the max and min value via Collections.min/max
section: Imported - java2s Archive
order: 1109
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-find-the-max-and-min-value-via-collectionsminmax.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array find the max and min value via Collections.min/max

```java title=Example.java
import java.util.Arrays;
import java.util.Collections;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Integer[] numbers = { 1238, 3212, 1236, 7321, 3450, 1345, 3454, 9, 5435, 1233 };

    System.out.println(Arrays.toString(numbers));
    //fromwww.java2s.comint min = (int) Collections.min(Arrays.asList(numbers));
    int max = (int) Collections.max(Arrays.asList(numbers));

    System.out.println("Min number: " + min);
    System.out.println("Max number: " + max);
  }
}
```

PreviousNext

## Related

- Java array fill random number within a range
- Java array fill unique random number
- Java array find the largest and smallest number using for loop
- Java array find the max and min value via sorting
- Java array get random element
