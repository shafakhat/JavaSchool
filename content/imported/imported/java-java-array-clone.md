---
title: Java array clone
nav: Java array clone
description: String[] array2 = { "CSS", "HTML", "Java", "Javascript", "SQL", "C++", "C" };
section: Imported - java2s Archive
order: 1099
source: https://web.archive.org/web/20210102113254/http://www.java2s.com/ref/java/java-array-clone.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array clone

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int[] array1 = { 1, 2, 3, 4, 5 };

    String[] array2 = { "CSS", "HTML", "Java", "Javascript", "SQL", "C++", "C" };

    System.out.println("Original size: " + array1.length);
    System.out.println("New size: " + cloneArray(array1).length);

    System.out.println("Original size: " + array2.length);
    System.out.println("New size: " + cloneArray(array2).length);
  }//www.java2s.comstaticint[] cloneArray(int[] original) {
    return (int[]) original.clone();
  }

  static <T> T[] cloneArray(T original[]) {
    return (T[]) original.clone();
  }
}
```

PreviousNext

## Related

- Java Array append a char to char array
- Java Array append String to String array
- Java array append new element
- Java array convert to List
- Java array copy to double its size
