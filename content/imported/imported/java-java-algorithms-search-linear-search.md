---
title: Java Algorithms Search Linear Search
nav: Java Algorithms Search Lin...
description: The linear search compares the key element sequentially with each element in the array.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-search-linear-search.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

The linear search compares the key element sequentially with each element in the array.

It continues to do so until the key matches an element in the array or the array is exhausted.

- If a match is found, the linear search returns the index of the element in the array that matches the key.
- If no match is found, the search returns -1.

```java title=Example.java
publicclass Main {
  /** The method for finding a key in the list */publicstaticint linearSearch(int[] list, int key) {
    for (int i = 0; i < list.length; i++) {
      if (key == list[i])
        return i;
    }/*www.java2s.com*/return -1;
  }

  publicstaticvoid main(String[] args) {
    int[] list = { 11, 14, 4, 12, 5, -3, 16, 2 };
    int i = linearSearch(list, 4);
    System.out.println(i);
    int j = linearSearch(list, -4);
    System.out.println(j);
    int k = linearSearch(list, -3);
    System.out.println(k);
  }
}
```

PreviousNext

## Related

- Java Algorithms Parse postfix arithmetic expressions
- Java Algorithms Reverse a String using Stack
- Java Algorithms Search Binary Search
- Java Algorithms Solve Towers of Hanoi puzzle
- Java Algorithms Sort Bubble Sort
