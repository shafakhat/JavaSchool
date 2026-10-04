---
title: Java OCA OCP Practice Question 1066
nav: Java OCA OCP Practice Ques...
description: The parseName() method is invoked within main() on a new Main object.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20210101014710/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1066.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following program?

```java title=Example.java

1:  publicclass Main {
2:    publicString name;
3:    publicvoid parseName() {
4:      System.out.print("1");
5:      try { //fromwww.java2s.com
6:        System.out.print("2");
7:        int x = Integer.parseInt(name);
8:        System.out.print("3");
9:      } catch (NumberFormatException e) {
10:       System.out.print("4");
11:     }
12:   }
13:   publicstaticvoid main(String[] args) {
14:     Main m = new Main();
15:     m.name = "Leroy";
16:     m.parseName();
17:     System.out.print("5");
18:   }
19:}
```

- A. 12
- B. 1234
- C. 1235
- D. 124
- E. 1245
- F. The code does not compile.
- G. An uncaught exception is thrown.

```java title=Example.java
E.
```

## Note

The parseName() method is invoked within main() on a new Main object.

Line 4 prints 1.

The try block executes and 2 is printed.

Line 7 throws a NumberFormatException, so line 8 doesn't execute.

The exception is caught on line 9, and line 10 prints 4.

Because the exception is handled, execution resumes normally.

parseName runs to completion, and line 17 executes, printing 5.

That's the end of the program, so the output is 1245.

PreviousNext

## Related

- Java OCA OCP Practice Question 1063
- Java OCA OCP Practice Question 1064
- Java OCA OCP Practice Question 1065
- Java OCA OCP Practice Question 1067
- Java OCA OCP Practice Question 1068
