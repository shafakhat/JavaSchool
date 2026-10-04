---
title: Java array shift left and right by one element
nav: Java array shift left and ...
description: //fromwww.java2s.com//shift right by one element, leave the left most unchangedSystem.arraycopy(array, 0, array, 1, array.length - 1);
section: Imported
order: 20010
source: http://www.java2s.com/ref/java/java-array-shift-left-and-right-by-one-element.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array shift left and right by one element

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] argv) throwsException {
    int[] array = { 1, 2, 3 ,4 , 5 , 6, 7,};
    //fromwww.java2s.com//shift right by one element, leave the left most unchangedSystem.arraycopy(array, 0, array, 1, array.length - 1);
    System.out.println(Arrays.toString(array));

    //shift left by one element, leave the right most unchanged
    array =newint[] { 1, 2, 3 ,4 , 5 , 6, 7,};
    System.arraycopy(array, 1, array, 0, array.length - 1);
    System.out.println(Arrays.toString(array));
  }
}
```

PreviousNext

## Related

- Java array length double
- Java array remove duplicate elements
- Java array reverse
- Java array shuffle
- Java array shuffle vis Collections.shuffle
