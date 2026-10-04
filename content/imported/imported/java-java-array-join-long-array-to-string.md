---
title: Java array join long[] array to String
nav: Java array join long[] arr...
description: long[] tokens = newlong[] { 34, 35, 36, 37, 37, 37, 67, 68, 69 };
section: Imported
order: 20000
source: http://www.java2s.com/ref/java/java-array-join-long-array-to-string.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array join long[] array to String

```java title=Example.java
//package com.demo2s;publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
        long[] tokens = newlong[] { 34, 35, 36, 37, 37, 37, 67, 68, 69 };
        String delimiter = "";
        System.out.println(joinLongs(tokens, delimiter));
    }//fromwww.java2s.com/**
     * Concatenates the given long[] array into one String, inserting a delimiter
     * between each pair of elements.
     */publicstaticString joinLongs(long[] tokens, String delimiter) {
        if (tokens == null)
            return"";
        StringBuilder result = newStringBuilder();

        for (int i = 0; i < tokens.length; i++) {
            if (i > 0 && delimiter != null) {
                result.append(delimiter);
            }
            result.append(String.valueOf(tokens[i]));
        }
        return result.toString();
    }

}
```

PreviousNext

## Related

- Java array get random element
- Java array get sub array
- Java array join int[] array to String
- Java array join String[] array to String
- Java array join to String with char separator
