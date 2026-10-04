---
title: Java OCA OCP Practice Question 1003
nav: Java OCA OCP Practice Ques...
description: Commas are used to separate statements within the initialization and iteration parts of a for statement.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20210101014700/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1003.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is wrong with the following for statement?

```java title=Example.java
for(i=0; j=0, i<10; ++i, j += i) {
    k += i*i + j*j;
}
```

- A. It should include more than one statement in the statement block.
- B. There should be a comma between i=0 and j=0.
- C. It uses more than one loop index.
- D. There should be a semicolon between j=0 and i<10.

```java title=Example.java
B and D.
```

## Note

Commas are used to separate statements within the initialization and iteration parts of a for statement.

Semicolons are used to separate the initialization, loop condition, and iteration parts of the for statement.

PreviousNext

## Related

- Java OCA OCP Practice Question 1000
- Java OCA OCP Practice Question 1001
- Java OCA OCP Practice Question 1002
- Java OCA OCP Practice Question 1004
- Java OCA OCP Practice Question 1005
