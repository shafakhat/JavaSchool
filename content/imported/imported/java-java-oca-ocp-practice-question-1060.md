---
title: Java OCA OCP Practice Question 1060
nav: Java OCA OCP Practice Ques...
description: What is the output of the following snippet, assuming a and b are both 0?
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1060.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following snippet, assuming a and b are both 0?

```java title=Example.java

3:     try {
4:       return a / b;
5:     } catch (RuntimeException e) {
6:       return -1;
7:     } catch (ArithmeticException e) {
8:       return 0;
9:     } finally {
10:      System.out.print("done");
11:    }
```

- A. -1
- B. 0
- C. done-1
- D. done0
- E. The code does not compile.
- F. An uncaught exception is thrown.

```java title=Example.java
E.
```

## Note

The order of catch blocks is important because they're checked in the order they appear after the try block.

Because ArithmeticException is a child class of RuntimeException, the catch block on line 7 is unreachable.

If an ArithmeticException is thrown in try try block, it will be caught on line 5.

Line 7 generates a compiler error because it is unreachable code.

PreviousNext

## Related

- Java OCA OCP Practice Question 1057
- Java OCA OCP Practice Question 1058
- Java OCA OCP Practice Question 1059
- Java OCA OCP Practice Question 1061
- Java OCA OCP Practice Question 1062
