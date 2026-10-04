---
title: Java Algorithms Search Binary Search
nav: Java Algorithms Search Bin...
description: For binary search to work, the elements in the array must be ordered.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-search-binary-search.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

For binary search to work, the elements in the array must be ordered.

Assume that the array is in ascending order.

The binary search first compares the key with the element in the middle of the array.

Consider the following three cases:

- If the key is less than the middle element, continue to search for the key only in the first half of the array.
- If the key is equal to the middle element, the search ends with a match.
- If the key is greater than the middle element, continue to search for the key only in the second half of the array.

```java title=Example.java
publicclass Main {
  /** Use binary search to find the key in the list */publicstaticint binarySearch(int[] list, int key) {
    int low = 0;//fromwww.java2s.comint high = list.length - 1;

    while (high >= low) {
      int mid = (low + high) / 2;
      if (key < list[mid])
        high = mid - 1;
      elseif (key == list[mid])
        return mid;
      else
        low = mid + 1;
    }

    return -low - 1; // Now high < low
  }

  publicstaticvoid main(String[] args) {
    int[] list = {-3,2, 4, 6, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79,100,109,200};
    int i = binarySearch(list, 2);
    System.out.println(i);

    int j = binarySearch(list, 11);
    System.out.println(j);
    int k = binarySearch(list, 12);
    System.out.println(k);
    int l = binarySearch(list, 1);
    System.out.println(l);
    int m = binarySearch(list, 30);
    System.out.println(m);

  }
}
```

PreviousNext

## Related

- Java Algorithms Move along circle
- Java Algorithms Parse postfix arithmetic expressions
- Java Algorithms Reverse a String using Stack
- Java Algorithms Search Linear Search
- Java Algorithms Solve Towers of Hanoi puzzle
