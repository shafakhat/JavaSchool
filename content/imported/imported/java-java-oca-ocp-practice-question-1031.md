---
title: Java OCA OCP Practice Question 1031
nav: Java OCA OCP Practice Ques...
description: 9: publicvoid print() { System.out.println("Square print"); }
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1031.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code?

```java title=Example.java

1: abstractclassPrintable {
2:   publicfinalvoid print() {
         System.out.println("Printable print");
     } //fromwww.java2s.com
3:     publicstaticvoid main(String[] args) {
4:       Printable p = new Square();
5:       p.print();
6:     }
7: }
8: publicclass Square extendsPrintable {
9:   publicvoid print() { System.out.println("Square print"); }
10:}
```

- A. Printable print
- B. Square print
- C. The code will not compile because of line 4.
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 9.

```java title=Example.java
E.
```

## Note

The code doesn't compile, so options A and B are incorrect.

The issue with line 9 is that print() is marked as final in the superclass Printable, which means it cannot be overridden. There are no errors on any other lines, so options C and D are incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1029
- Java OCA OCP Practice Question 1030
- Java OCA OCP Practice Question 1032
- Java OCA OCP Practice Question 1033
