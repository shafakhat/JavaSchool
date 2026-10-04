---
title: Java array get sub array
nav: Java array get sub array
description: /*fromwww.java2s.com*/System.out.println(Arrays.toString(b));
section: Imported
order: 20001
source: http://www.java2s.com/ref/java/java-array-get-sub-array.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array get sub array

```java title=Example.java
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] argv) {
    byte[] b = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    byte[] c = get(b, 3);
    byte[] d = get(b, 3, 3);
    /*fromwww.java2s.com*/System.out.println(Arrays.toString(b));
    System.out.println(Arrays.toString(c));
    System.out.println(Arrays.toString(d));
  }

  /**
   * Gets the subarray from <tt>array</tt> that starts at <tt>offset</tt>.
   */publicstaticbyte[] get(byte[] array, int offset) {
    return get(array, offset, array.length - offset);
  }

  /**
   * Gets the subarray of length <tt>length</tt> from <tt>array</tt> that starts
   * at <tt>offset</tt>.
   */publicstaticbyte[] get(byte[] array, int offset, int length) {
    byte[] result = newbyte[length];
    System.arraycopy(array, offset, result, 0, length);
    return result;
  }
}
```

PreviousNext

## Related

- Java array find the max and min value via Collections.min/max
- Java array find the max and min value via sorting
- Java array get random element
- Java array join int[] array to String
- Java array join long[] array to String
