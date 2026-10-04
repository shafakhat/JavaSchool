---
title: Java OCA OCP Practice Question 104
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 104
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20210101014437/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-104.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Given:

```java title=Example.java
class Animal { /*fromwww.java2s.com*/privatevoid fly() {
     System.out.print("bang ");
  }
}
publicclass Bird extends Animal {
  publicstaticvoid main(String[] args) {
    new Bird().go();
  }
  void go() {
    fly();
    // Animal.fly();  // line A
  }
  privatevoid fly() { System.out.print("sh-bang "); }
}
```

Which are true? (Choose all that apply.)

- A. The output is bang
- B. The output is sh-bang
- C. Compilation fails.
- D. If line A is uncommented, the output is bang bang
- E. If line A is uncommented, the output is sh-bang bang
- F. If line A is uncommented, compilation fails.

```java title=Example.java
B and F are correct.
```

## Note

Since Animal.fly() is private, it can't be overridden.

It is invisible to class Bird.

A, C, D, and E are incorrect based on the above.

PreviousNext

## Related

- Java OCA OCP Practice Question 101
- Java OCA OCP Practice Question 102
- Java OCA OCP Practice Question 103
- Java OCA OCP Practice Question 105
- Java OCA OCP Practice Question 106
