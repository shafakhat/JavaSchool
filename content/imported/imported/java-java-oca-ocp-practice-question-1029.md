---
title: Java OCA OCP Practice Question 1029
nav: Java OCA OCP Practice Ques...
description: Concrete classes are, by definition, not abstract, so option A is incorrect.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1029.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which of the following is true about a concrete subclass?

Choose all that apply

- A. A concrete subclass can be declared as abstract.
- B. A concrete subclass must implement all inherited abstract methods.
- C. A concrete subclass must implement all methods defined in an inherited interface.
- D. A concrete subclass cannot be marked as final.
- E. Abstract methods cannot be overridden by a concrete subclass.

```java title=Example.java
B.
```

## Note

Concrete classes are, by definition, not abstract, so option A is incorrect.

A concrete class must implement all inherited abstract methods, so option B is correct.

Option C is incorrect; a superclass may have already implemented an inherited interface, so the concrete subclass would not need to implement the method.

Concrete classes can be both final and not final, so option D is incorrect.

Finally, abstract methods must be overridden by a concrete subclass, so option E is incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1030
- Java OCA OCP Practice Question 1031
