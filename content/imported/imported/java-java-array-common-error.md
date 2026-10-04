---
title: Java Array Common Error
nav: Java Array Common Error
description: Imported from the java2s.com archive: Java Array Common Error
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/20210102113251/http://www.java2s.com/ref/java/java-array-common-error.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Identify and fix the errors in the following code:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
     double[100] r;

     for (int i = 0; i < r.length(); i++);
         r(i) = Math.random * 100;
  }
}
```

```java title=Example.java
public class Main {
  public static void main(String[] args) {

     double[100] r; //should be double[] r = new double[100];

                           //no ()
     for (int i = 0; i < r.length(); i++); // no ;
         r(i) = Math.random * 100;
       //r[i]       missing()
  }
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {

     double[] r = newdouble[100];

        //fromwww.java2s.comfor (int i = 0; i < r.length; i++)
         r[i] = Math.random() * 100;
  }
}
```

PreviousNext

## Related

- Java Array select random cards from deck
- Java Array shift elements
- Java Array sum all elements
- Java Array multidimensional Arrays
- Java Array multidimensional Arrays declaration
