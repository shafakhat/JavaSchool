---
title: Java Arithmetic Operator sum a list of numbers
nav: Java Arithmetic Operator s...
description: Imported from the java2s.com archive: Java Arithmetic Operator sum a list of numbers
section: Imported - java2s Archive
order: 1089
source: https://web.archive.org/web/20210102113220/http://www.java2s.com/ref/java/java-arithmetic-operator-sum-a-list-of-numbers.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that displays the result of

```java title=Example.java

1 +  2  +  3  +  4  +  5  +  6  +  7  + 8  +  9
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9);
  }
}
```

## Note

We can also use a for loop:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int result = 0;
    for (int i = 1; i <= 9; i++) {
      result += i;//www.java2s.com
    }
    System.out.println(result);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator separate the Digits in an Integer
- Java Arithmetic Operator solve 2 by 2 linear equations
- Java Arithmetic Operator solve quadratic equations
- Java Arithmetic Operator sum the digits in an integer
- Java Boolean Logical Operators truth table
