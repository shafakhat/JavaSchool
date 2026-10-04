---
title: Java OCA OCP Practice Question 1036
nav: Java OCA OCP Practice Ques...
description: What is the output of the following code? (Choose all that apply)
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1036.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code? (Choose all that apply)

```java title=Example.java

1: interfaceArea {
2:   publicdefaultint getArea(int input) { return 2; }
3: } //fromwww.java2s.com
4: publicclass Square implementsArea {
5:   publicString getArea() { return"4"; }
6:   publicString getArea(int input) { return"6"; }
7:   publicstaticvoid main(String[] args) {
8:     System.out.println(new Square().getArea(-1));
9:   }
10: }
```

- A. 2
- B. 4
- C. 6
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 6.
- F. The code will not compile because of line 8.

```java title=Example.java
E.
```

## Note

The code doesn't compile because line 6 contains an incompatible override of the getArea(int input) method defined in the Area interface.

In particular, int and String are not covariant returns types, since int is not a subclass of String.

Note that line 5 compiles without issue; getArea() is an overloaded method that is not related to the parent interface method that takes an int value.

PreviousNext

## Related

- Java OCA OCP Practice Question 1033
- Java OCA OCP Practice Question 1034
- Java OCA OCP Practice Question 1035
- Java OCA OCP Practice Question 1037
- Java OCA OCP Practice Question 1038
