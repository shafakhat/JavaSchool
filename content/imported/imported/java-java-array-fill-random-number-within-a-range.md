---
title: Java array fill random number within a range
nav: Java array fill random num...
description: Imported from the java2s.com archive: Java array fill random number within a range
section: Imported - java2s Archive
order: 1104
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-fill-random-number-within-a-range.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array fill random number within a range

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = newint[10];
    Random rand = newRandom();
    for (int i = 0; i < array.length; i++) {
      array[i] = rand.nextInt(10);//fromwww.java2s.com
    }
    System.out.println(Arrays.toString(array));

  }
}
```

PreviousNext

## Related

- Java array copy to merge two arrays
- Java array copy using System.arraycopy()
- Java array fill random number
- Java array fill unique random number
- Java array find the largest and smallest number using for loop
