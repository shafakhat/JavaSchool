---
title: Java OCA OCP Practice Question 1014
nav: Java OCA OCP Practice Ques...
description: The interface variable amount is correctly declared, with public and static being assumed and automatically inserted by the compiler, so option B is incorrect.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20210101014702/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1014.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Choose the correct statement about the following code:

```java title=Example.java

1: publicinterface Pet {
2:   int amount = 10;
3:   publicstaticvoid eatGrass();
4:   publicint chew() {
5:     return 13;
6:   }
7: }
```

- A. It compiles and runs without issue.
- B. The code will not compile because of line 2.
- C. The code will not compile because of line 3.
- D. The code will not compile because of line 4.
- E. The code will not compile because of lines 2 and 3.
- F. The code will not compile because of lines 3 and 4.

```java title=Example.java
F.
```

## Note

The interface variable amount is correctly declared, with public and static being assumed and automatically inserted by the compiler, so option B is incorrect.

The method declaration for eatGrass() on line 3 is incorrect because the method has been marked as static but no method body has been provided.

The method declaration for chew() on line 4 is also incorrect, since an interface method that provides a body must be marked as default or static explicitly.

Therefore, option F is the correct answer since this code contains two compile-time errors.

PreviousNext

## Related

- Java OCA OCP Practice Question 1011
- Java OCA OCP Practice Question 1012
- Java OCA OCP Practice Question 1013
- Java OCA OCP Practice Question 1015
- Java OCA OCP Practice Question 1016
