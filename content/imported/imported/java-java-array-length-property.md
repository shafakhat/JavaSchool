---
title: Java Array length property
nav: Java Array length property
description: The size of an array is the number of elements that an array is holding.
section: Imported
order: 20005
source: http://www.java2s.com/ref/java/java-array-length-property.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Java arrays are implemented as objects.

The size of an array is the number of elements that an array is holding.

We can access array length via its length instance variable.

Here is a program that demonstrates this property:

```java title=Example.java
// demonstrates the length array member.publicclass Main {
  publicstaticvoid main(String args[]) {
    int a1[] = newint[10];
    int a2[] = {3, 5, 7, 1, 8, 99, 44, -10};
    int a3[] = {4, 3, 2, 1};

    System.out.println("length of a1 is " + a1.length);
    System.out.println("length of a2 is " + a2.length);
    System.out.println("length of a3 is " + a3.length);
  }//www.java2s.com
}
```

The following code uses length properties in a for loop.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int a[] = {3, 5, 7, 1, 8, 99, 44, -10};
    for(int i=0;i<a.length;i++) {
      System.out.println(a[i]);//fromwww.java2s.com
    }

  }
}
```

PreviousNext

## Related

- Java Enumeration Type with validator
- Java Array Type
- Java Array Initializer
- Java Array as frequency counters
- Java Array count occurrences of letter in char array
