---
title: Java array reverse
nav: Java array reverse
description: }/*fromwww.java2s.com*/System.out.println(Arrays.toString(array));
section: Imported
order: 20009
source: http://www.java2s.com/ref/java/java-array-reverse.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array reverse

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    System.out.println(Arrays.toString(array));
    int arrayLength = array.length;
    for (int i = 0; i < arrayLength - 1; i++) {
      int temp = array[i];
      array[i] = array[arrayLength - 1 - i];
      array[arrayLength - 1 - i] = temp;
    }/*fromwww.java2s.com*/System.out.println(Arrays.toString(array));

  }
}
```

PreviousNext

## Related

- Java array join to String with String separator
- Java array length double
- Java array remove duplicate elements
- Java array shift left and right by one element
- Java array shuffle
