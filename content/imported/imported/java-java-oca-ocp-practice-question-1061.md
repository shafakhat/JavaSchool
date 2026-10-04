---
title: Java OCA OCP Practice Question 1061
nav: Java OCA OCP Practice Ques...
description: A. is correct. calling such methods do not change this object.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1061.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

In java, Strings are immutable.

A direct implication of this is...

Select 2 options

- A. you cannot call methods like "1234".replace(' 1', '9'); and expect to change the original String.
- B. you cannot change a String object, once it is created.
- C. you can change a String object only by the means of its methods.
- D. you cannot extend String class.
- E. you cannot compare String objects.

```java title=Example.java
Correct Options are: A B
```

## Note

A. is correct. calling such methods do not change this object.

They create a new String object.

You can have a final class whose objects are mutable.

String class implements Comparable interface.

PreviousNext

## Related

- Java OCA OCP Practice Question 1058
- Java OCA OCP Practice Question 1059
- Java OCA OCP Practice Question 1060
- Java OCA OCP Practice Question 1062
- Java OCA OCP Practice Question 1063
