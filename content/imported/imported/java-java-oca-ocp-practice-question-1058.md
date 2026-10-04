---
title: Java OCA OCP Practice Question 1058
nav: Java OCA OCP Practice Ques...
description: What is printed besides the stack trace caused by the NullPointerException from line 16?
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1058.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is printed besides the stack trace caused by the NullPointerException from line 16?

```java title=Example.java

1: publicclass Main {
2:   publicvoid go() {
3:     System.out.print("A");
4:     try { //www.java2s.com
5:         stop();
6:     } catch (ArithmeticException e) {
7:         System.out.print("B");
8:     } finally {
9:         System.out.print("C");
10:    }
11:    System.out.print("D");
12:  }
13:  publicvoid stop() {
14:    System.out.print("E");
15:    Object x = null;
16:    x.toString();
17:    System.out.print("F");
18:  }
19:  publicstaticvoid main(String[] args) {
20:    new Main().go();
21:  }
22: }
```

```java title=Example.java

A.  AE
B.  AEBCD
C.  AEC
D.  AECD
E.  No output appears other than the stack trace.
```

```java title=Example.java
C.
```

## Note

The main() method invokes go and A is printed on line 3.

The stop method is invoked and E is printed on line 14.

Line 16 throws a NullPointerException, so stop immediately ends and line 17 doesn't execute.

The exception isn't caught in go, so the go method ends as well, but not before its finally block executes and C is printed on line 9.

Because main() doesn't catch the exception, the stack trace displays and no further output occurs, so AEC was the output printed before the stack trace.

PreviousNext

## Related

- Java OCA OCP Practice Question 1055
- Java OCA OCP Practice Question 1056
- Java OCA OCP Practice Question 1057
- Java OCA OCP Practice Question 1059
- Java OCA OCP Practice Question 1060
