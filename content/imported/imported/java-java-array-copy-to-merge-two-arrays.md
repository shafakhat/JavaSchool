---
title: Java array copy to merge two arrays
nav: Java array copy to merge t...
description: Imported from the java2s.com archive: Java array copy to merge two arrays
section: Imported - java2s Archive
order: 1101
source: https://web.archive.org/web/20210102113254/http://www.java2s.com/ref/java/java-array-copy-to-merge-two-arrays.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array copy to merge two arrays

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] names = newString[] { "HTML", "CSS", "SQL" };

    String[] extended = newString[5];

    extended[0] = "0";
    extended[1] = "1";
    extended[2] = "2";
    extended[3] = "3";
    extended[4] = "4";

    System.arraycopy(names, 0, extended, 0, names.length);

    System.out.println(Arrays.toString(names));
    System.out.println(Arrays.toString(extended));
  }//fromwww.java2s.com
}
```

PreviousNext

## Related

- Java array clone
- Java array convert to List
- Java array copy to double its size
- Java array copy using System.arraycopy()
- Java array fill random number
