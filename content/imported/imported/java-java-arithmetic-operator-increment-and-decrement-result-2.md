---
title: Java Arithmetic Operator increment and decrement result 2
nav: Java Arithmetic Operator i...
description: The prefixed operator causes the value of the x variable to be changed before the expression is evaluated.
section: Imported - java2s Archive
order: 1075
source: https://web.archive.org/web/20210102113217/http://www.java2s.com/ref/java/java-arithmetic-operator-increment-and-decrement-result-2.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code?

```java title=Example.java
int x = 3;
int answer = ++x * 10;
```

```java title=Example.java
40
```

## Note

The prefixed operator causes the value of the x variable to be changed before the expression is evaluated.

The statement int?answer = ++x * 10 does the same thing, in order, as these statements:

```java title=Example.java

x++;
int answer = x * 10;
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int x = 3;//www.java2s.comint answer = ++x * 10;
    System.out.println(answer);

  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator divisible by 3
- Java Arithmetic Operator find the number of years
- Java Arithmetic Operator increment and decrement result 1
- Java Arithmetic Operator Integer division
- Java Arithmetic Operator Question 1
