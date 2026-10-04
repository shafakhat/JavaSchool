---
title: Java OCA OCP Practice Question 1009
nav: Java OCA OCP Practice Ques...
description: The case values must evaluate to integer values during compilation.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1009.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is wrong with the following switch statement?

```java title=Example.java
switch(i == 10) {
     case'1':
         ++i;  //www.java2s.combreak;
     case"2":
         --i;
     case 3:
         i *= 5;
         break;
     default
        i %= 3;
}
```

- A. The switch expression must evaluate to an integer value.
- B. The first case specifies a char value.
- C. The second case specifies a String value.
- D. There is a break statement missing in the second case.
- E. An : should follow default.

```java title=Example.java
A, C, and E.
```

## Note

The switch condition must be an integer expression.

The case values must evaluate to integer values during compilation.

A : should follow the default label.

PreviousNext

## Related

- Java OCA OCP Practice Question 1006
- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1008
- Java OCA OCP Practice Question 1010
- Java OCA OCP Practice Question 1011
