---
title: Java autoboxing unboxing in method calling and returning
nav: Java autoboxing unboxing i...
description: Autoboxing happens when a primitive type must be converted into an object.
section: Imported
order: 20045
source: http://www.java2s.com/ref/java/java-autoboxing-unboxing-in-method-calling-and-returning.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Autoboxing happens when a primitive type must be converted into an object.

Auto-unboxing happens when an object must be converted into a primitive type.

Autoboxing/unboxing might happen in an argument passed, or a value returning.

```java title=Example.java
publicclass Main {
  staticint m(Integer v) {
    return v ; // auto-unbox to int
  }  /*fromwww.java2s.com*/publicstaticvoid main(String args[]) {
    Integer iOb = m(100);

    System.out.println(iOb);
  }
}
```

PreviousNext

## Related

- Java array sort elements
- Java Array Linear Search
- Java autoboxing unboxing
- Java autoboxing unboxing in expressions
- Java autoboxing unboxing in switch statement
