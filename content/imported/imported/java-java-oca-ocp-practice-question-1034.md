---
title: Java OCA OCP Practice Question 1034
nav: Java OCA OCP Practice Ques...
description: The code compiles and runs without issues, so Options C and D are incorrect.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1034.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following application?

```java title=Example.java
package mypkg; /*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] dribble) {
     try {
        System.out.print(1);
        thrownewClassCastException();
     } catch (ArrayIndexOutOfBoundsException ex) {
        System.out.print(2);
     } catch (Throwable ex) {
        System.out.print(3);
     } finally {
        System.out.print(4);
     }
     System.out.print(5);
  }
}
```

- A. 1345
- B. 1235
- C. The code does not compile.
- D. The code compiles but throws an exception at runtime.

```java title=Example.java
A.
```

## Note

The code compiles and runs without issues, so Options C and D are incorrect.

The try block throws a ClassCastException.

Since ClassCastException is not a subclass of ArrayIndexOutOfBoundsException, the first catch block is skipped.

For the second catch block, ClassCastException is a subclass of Throwable, so that block is executed.

Then, the finally block is executed and then control returns to the main() method with no exception being thrown.

The result is that 1345 is printed, making Option A the correct answer.

PreviousNext

## Related

- Java OCA OCP Practice Question 1031
- Java OCA OCP Practice Question 1032
- Java OCA OCP Practice Question 1033
- Java OCA OCP Practice Question 1035
- Java OCA OCP Practice Question 1036
