---
title: Java OCA OCP Practice Question 1063
nav: Java OCA OCP Practice Ques...
description: Line 6 catches the exception, line 7 prints Problem, and then line 8 calls System.exit, which terminates the JVM.
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1063.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following program?

```java title=Example.java

1: publicclass Main {
2:   publicvoid start() {
3:    try { //www.java2s.com
4:      System.out.print("Starting up ");
5:      thrownewException();
6:    } catch (Exception e) {
7:       System.out.print("Problem ");
8:       System.exit(0);
9:    } finally {
10:      System.out.print("Shutting down ");
11:   }
12:  }
13:  publicstaticvoid main(String[] args) {
14:    new Main().start();
15:  }
16:}
```

- A. Starting up
- B. Starting up Problem
- C. Starting up Problem Shutting down
- D. Starting up Shutting down
- E. The code does not compile.
- F. An uncaught exception is thrown.

```java title=Example.java
B.
```

## Note

The main() method invokes start on a new Main object.

Line 4 prints Starting up; then line 5 throws an Exception.

Line 6 catches the exception, line 7 prints Problem, and then line 8 calls System.exit, which terminates the JVM.

The finally block does not execute because the JVM is no longer running.

PreviousNext

## Related

- Java OCA OCP Practice Question 1060
- Java OCA OCP Practice Question 1061
- Java OCA OCP Practice Question 1062
- Java OCA OCP Practice Question 1064
- Java OCA OCP Practice Question 1065
