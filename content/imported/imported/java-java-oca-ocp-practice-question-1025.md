---
title: Java OCA OCP Practice Question 1025
nav: Java OCA OCP Practice Ques...
description: 2: publicvoid printName(double input) { System.out.print("Printable"); }
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1025.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code?

```java title=Example.java

1: classPrintable
2:   publicvoid printName(double input) { System.out.print("Printable"); }
3: } //www.java2s.com
4: publicclass Main extendsPrintable {
5:   publicvoid printName(int input) { System.out.print("Main"); }
6:   publicstaticvoid main(String[] args) {
7:     Main m = new Main();
8:     m.printName(4);
9:     m.printName(9.0);
10:   }
11: }
```

```java title=Example.java

A.  MainPrintable
B.  PrintableMain
C.  MainMain
D.  PrintablePrintable
E.  The code will not compile because of line 5.
F.  The code will not compile because of line 9.
```

```java title=Example.java
A.
```

## Note

The code compiles and runs without issue, so options E and F are incorrect.

The printName() method is an overload in Main, not an override, so both methods may be called.

The call on line 8 references the version that takes an int as input defined in the Main class, and the call on line 9 references the version in the Printable class that takes a double.

Therefore, MainPrintable is output and option A is the correct answer.

PreviousNext

## Related

- Java OCA OCP Practice Question 1022
- Java OCA OCP Practice Question 1023
- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1027
