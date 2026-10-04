---
title: Java OCA OCP Practice Question 1056
nav: Java OCA OCP Practice Ques...
description: What will happen if you add the statement System.out.println(5 / 0); to a working main() method?
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20210101014708/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1056.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What will happen if you add the statement System.out.println(5 / 0); to a working main() method?

- A. It will not compile.
- B. It will not run.
- C. It will run and throw an ArithmeticException.
- D. It will run and throw an IllegalArgumentException.
- E. None of the above.

```java title=Example.java
C.
```

## Note

The compiler tests the operation for a valid type but not a valid result, so the code will still compile and run.

At runtime, evaluation of the parameter takes place before passing it to the print() method, so an ArithmeticException object is raised.

PreviousNext

## Related

- Java OCA OCP Practice Question 1053
- Java OCA OCP Practice Question 1054
- Java OCA OCP Practice Question 1055
- Java OCA OCP Practice Question 1057
- Java OCA OCP Practice Question 1058
