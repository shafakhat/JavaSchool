---
title: Java Array append a char to char array
nav: Java Array append a char t...
description: char[] c = newchar[] { 'd', 'e', 'm', 'o', '2', 's', '.', 'c', 'o', 'm' };
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20210102113253/http://www.java2s.com/ref/java/java-array-append-a-char-to-char-array.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Array append a char to char array

```java title=Example.java
//package com.demo2s;publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
        char[] c = newchar[] { 'd', 'e', 'm', 'o', '2', 's', '.', 'c', 'o', 'm' };
        char toAdd = 'a';
        System.out.println(java.util.Arrays.toString(addChar(c, toAdd)));
    }/*fromwww.java2s.com*//**
     * Adds a char to an array of chars and returns the new array.
     *
     * @param c The chars to where the new char should be appended
     * @param toAdd the char to be added
     * @return a new array with the passed char appended.
     */publicstaticchar[] addChar(char[] c, char toAdd) {
        char[] c1 = newchar[c.length + 1];

        System.arraycopy(c, 0, c1, 0, c.length);
        c1[c.length] = toAdd;
        return c1;

    }
}
```

PreviousNext

## Related

- Java Array multidimensional Arrays reference element
- Java Array search unsorted array for a value using for each loop
- Java array check if an array of primitive chars is empty or null.
- Java Array append String to String array
- Java array append new element
