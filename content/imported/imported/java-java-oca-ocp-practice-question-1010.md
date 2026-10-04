---
title: Java OCA OCP Practice Question 1010
nav: Java OCA OCP Practice Ques...
description: Which of the following may only be hidden and not overridden?
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1010.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which of the following may only be hidden and not overridden?

Choose all that apply

- A. private instance methods
- B. protected instance methods
- C. public instance methods
- D. static methods
- E. public variables
- F. private variables

```java title=Example.java
A, D, E, F.
```

## Note

First off, options B and C are incorrect because protected and public methods may be overridden, not hidden.

Option A is correct because private methods are always hidden in a subclass.

Option D is also correct because static methods cannot be overridden, only hidden.

Options E and F are correct because variables may only be hidden, regardless of the access modifier.

PreviousNext

## Related

- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1008
- Java OCA OCP Practice Question 1009
- Java OCA OCP Practice Question 1011
- Java OCA OCP Practice Question 1012
