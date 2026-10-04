---
title: Java OCA OCP Practice Question 1006
nav: Java OCA OCP Practice Ques...
description: Which of the following statements can be inserted in the blank line so that the code will compile successfully? (Choose all that apply)
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1006.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which of the following statements can be inserted in the blank line so that the code will compile successfully? (Choose all that apply)

```java title=Example.java
publicinterfacePrintable {}
publicclassShapeimplementsPrintable {
   publicstaticvoid main(String[] args) {
          frog = new Square();
   }
}

publicclassRectangleextendsShape {}
publicclass Square extendsShape {}
```

- A. Shape
- B. Square
- C. Rectangle
- D. Printable
- E. Object
- F. Long

```java title=Example.java
A, B, D, E.
```

## Note

The blank can be filled with any class or interface that is a super type of Square.

Option A is a superclass of Square, and option B is the same class, so both are correct.

Rectangle is not a superclass of Square, so option C is incorrect.

Square inherits the Printable interface, so option D is correct.

All classes inherit Object, so option E is correct.

Finally, Long is an unrelated class that is not a superclass of Square, and is therefore incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1003
- Java OCA OCP Practice Question 1004
- Java OCA OCP Practice Question 1005
- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1008
