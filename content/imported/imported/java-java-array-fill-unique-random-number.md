---
title: Java array fill unique random number
nav: Java array fill unique ran...
description: //check if the check array index has been set//if set regenerate while (check[rnd]) {
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-fill-unique-random-number.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array fill unique random number

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {
  publicstaticint[] uniqueRandom(int length) {
    Random rand = newRandom();
    int[] nums = newint[length];
    //fromwww.java2s.comboolean[] check = newboolean[length];

    for (int k = 0; k < length; k++) {
      int rnd = rand.nextInt(length);
      //check if the check array index has been set//if set regenerate while (check[rnd]) {
        rnd = rand.nextInt(length);
      }
      nums[k] = rnd;
      check[rnd] = true;
    }
    return nums;
  }
  publicstaticvoid main(String args[]) {
    int length = 10;
    int[] a = uniqueRandom(length);
    System.out.println(Arrays.toString(a));

  }
}
```

PreviousNext

## Related

- Java array copy using System.arraycopy()
- Java array fill random number
- Java array fill random number within a range
- Java array find the largest and smallest number using for loop
- Java array find the max and min value via Collections.min/max
