---
title: Java OCA OCP Practice Question 1070
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 1070
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20210101014711/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1070.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which of the following statements is/are true?

Select 1 option

- A. Subclasses must define all the abstract methods that the superclass defines.
- B. A class implementing an interface must define all the methods of that interface.
- C. A class cannot override the super class's constructor.
- D. It is possible for two classes to be the superclass of each other.
- E. An interface can implement multiple interfaces.

```java title=Example.java
Correct Option is  : C
```

## Note

A. is wrong. Not if the subclass is also defined abstract!

B. is wrong. Not if the class is defined abstract.

C. is correct. Because constructors are not inherited.

D. and E. are wrong.

Interface cannot "implement" anything.

It can extend multiple interfaces.

The following is a valid declaration:

```java title=Example.java
interface I1 extends I2, I3, I4  {  }
```

PreviousNext

## Related

- Java OCA OCP Practice Question 1067
- Java OCA OCP Practice Question 1068
- Java OCA OCP Practice Question 1069
- Java OCA OCP Practice Question 1071
- Java OCA OCP Practice Question 1072
