---
title: Java OCA OCP Practice Question 1019
nav: Java OCA OCP Practice Ques...
description: Which statements are true for both abstract classes and interfaces?
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20210101014703/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1019.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which statements are true for both abstract classes and interfaces?

Choose all that apply

- A. All methods within them are assumed to be abstract.
- B. Both can contain public static final variables.
- C. Both can be extended using the extend keyword.
- D. Both can contain default methods.
- E. Both can contain static methods.
- F. Neither can be instantiated directly.
- G. Both inherit java.lang.Object.

```java title=Example.java
B, C, E, F.
```

## Note

Option A is wrong, because an abstract class may contain concrete methods.

Since Java 8, interfaces may also contain concrete methods in form of static or default methods.

Although all variables in interfaces are assumed to be public static final, abstract classes may contain them as well, so option B is correct.

Both abstract classes and interfaces can be extended with the extends keyword, so option C is correct.

Only interfaces can contain default methods, so option D is incorrect.

Both abstract classes and interfaces can contain static methods, so option E is correct.

Both structures require a concrete subclass to be instantiated, so option F is correct.

Finally, though an instance of an object that implements an interface inherits java.lang.Object, the interface itself doesn't; otherwise, Java would support multiple inheritance for objects, which it doesn't. Therefore, option G is incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1016
- Java OCA OCP Practice Question 1017
- Java OCA OCP Practice Question 1018
- Java OCA OCP Practice Question 1020
- Java OCA OCP Practice Question 1021
