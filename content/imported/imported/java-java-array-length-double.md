---
title: Java array length double
nav: Java array length double
description: Imported from java2s.com: Java array length double
section: Imported
order: 20006
source: http://www.java2s.com/ref/java/java-array-length-double.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array length double

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main (String args[]) {
    int array1[] = {1, 2, 3, 4, 5};

    System.out.println("Original size: " + array1.length);
    System.out.println(Arrays.toString(array1));
    //fromwww.java2s.com
    array1 = doubleArraySize(array1);

    System.out.println("New size: " + array1.length);
    System.out.println(Arrays.toString(array1));

  }
  publicstaticint[] doubleArraySize(int original[]) {
    int length = original.length;
    int newArray[] = newint[length*2];
    System.arraycopy(original, 0, newArray, 0, length);
    return newArray;
  }
}
```

PreviousNext

## Related

- Java array join String[] array to String
- Java array join to String with char separator
- Java array join to String with String separator
- Java array remove duplicate elements
- Java array reverse
