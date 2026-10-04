---
title: Java OCA OCP Practice Question 1023
nav: Java OCA OCP Practice Ques...
description: This code compiles and runs without issue, outputting false, so option B is the correct answer.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20210101014703/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1023.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code?

```java title=Example.java

1: interface Checkable {
2:   defaultboolean check() { return true; }
3: } //fromwww.java2s.com
4: publicclass Main implements Checkable {
5:   publicboolean check() { return false; }
6:     publicstaticvoid main(String[] args) {
7:     Checkable nocturnal = (Checkable)new Main();
8:     System.out.println(nocturnal.check());
9:     }
10: }
```

- A. true
- B. false
- C. The code will not compile because of line 2.
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 7.
- F. The code will not compile because of line 8.

```java title=Example.java
B.
```

## Note

This code compiles and runs without issue, outputting false, so option B is the correct answer.

The first declaration of check() is as a default interface method, assumed public.

The second declaration of check() correctly overrides the default interface method.

Finally, the newly created Main instance may be automatically cast to a Checkable reference without an explicit cast, although adding it doesn't break the code.

PreviousNext

## Related

- Java OCA OCP Practice Question 1020
- Java OCA OCP Practice Question 1021
- Java OCA OCP Practice Question 1022
- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1025
