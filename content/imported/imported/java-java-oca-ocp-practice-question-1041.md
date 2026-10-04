---
title: Java OCA OCP Practice Question 1041
nav: Java OCA OCP Practice Ques...
description: 2: privatevoid fly() { System.out.println("Shape is flying"); }
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20210101014706/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1041.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the result of the following code?

```java title=Example.java

1: publicabstractclassShape {
2:   privatevoid fly() { System.out.println("Shape is flying"); }
3:   publicstaticvoid main(String[] args) {
4:     Shape bird = newRectangle();
5:     bird.fly(); /*www.java2s.com*/
6:   }
7: }
8: classRectangleextendsShape {
9:   protectedvoid fly() { System.out.println("Rectangle is flying"); }
10: }
```

- A. Shape is flying
- B. Rectangle is flying
- C. The code will not compile because of line 4.
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 9.

```java title=Example.java
A.
```

## Note

The code compiles and runs without issue, so options C, D, and E are incorrect.

The trick here is that the method fly() is marked as private in the parent class Shape, which means it may only be hidden, not overridden.

With hidden methods, the specific method used depends on where it is referenced.

Since it is referenced within the Shape class, the method declared on line 2 was used, and option A is correct.

Alternatively, if the method was referenced within the Rectangle class, or if the method in the parent class was marked as protected and overridden in the subclass, then the method on line 9 would have been used.

PreviousNext

## Related

- Java OCA OCP Practice Question 1038
- Java OCA OCP Practice Question 1039
- Java OCA OCP Practice Question 1040
- Java OCA OCP Practice Question 1042
- Java OCA OCP Practice Question 1043
