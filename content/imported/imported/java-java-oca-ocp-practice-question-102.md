---
title: Java OCA OCP Practice Question 102
nav: Java OCA OCP Practice Ques...
description: What is the result of compiling and executing the following class?
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20210101014437/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-102.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the result of compiling and executing the following class?

```java title=Example.java
package sports; //fromwww.java2s.compublicclass MyClass {
        String color = "red";
        privatevoid printColor(String color) {
           color = "purple";
           System.out.print(color);
        }
        publicstaticvoid main(String[] rider) {
           new MyClass().printColor("blue");
        }
}
```

- A. red
- B. purple
- C. blue
- D. It does not compile.

```java title=Example.java
B.
```

## Note

First off, the color variable defined in the instance and set to red is ignored in the method printColor() as local scope overrides instance scope, so Option A is incorrect.

The value of color passed to the printColor() method is blue, but that is lost by the assignment to purple, making Option B the correct answer and Option C incorrect.

Option D is incorrect as the code compiles and runs without issue.

PreviousNext

## Related

- Java OCA OCP Practice Question 99
- Java OCA OCP Practice Question 100
- Java OCA OCP Practice Question 101
- Java OCA OCP Practice Question 103
- Java OCA OCP Practice Question 104
