---
title: Java OCA OCP Practice Question 10
nav: Java OCA OCP Practice Ques...
description: Which of the following may appear in a subclass of Fish named Tuna that is not in the mypkg package?
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20210101014422/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-10.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Given the following class:

```java title=Example.java
package mypkg;
publicclass Fish {
     protectedint size;
     protectedvoid swim() { }
}
```

Which of the following may appear in a subclass of Fish named Tuna that is not in the mypkg package?

- A. void swim() { }
- B. public void swim() { }
- C. size = 12;
- D. (new Tuna() ).size = 12;

```java title=Example.java
B, C.
```

## Note

A is illegal because it attempts to override the swim() method with a more restricted access mode.

B overrides with a less-restricted access mode, which is legal.

C is legal because it accesses protected superclass data of the current instance.

D is illegal because it accesses protected superclass data of a different instance.

PreviousNext

## Related

- Java OCA OCP Practice Question 7
- Java OCA OCP Practice Question 8
- Java OCA OCP Practice Question 9
- Java OCA OCP Practice Question 11
- Java OCA OCP Practice Question 12
