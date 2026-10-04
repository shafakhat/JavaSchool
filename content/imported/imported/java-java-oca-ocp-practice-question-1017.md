---
title: Java OCA OCP Practice Question 1017
nav: Java OCA OCP Practice Ques...
description: Although the definition of methods on lines 2 and 5 vary, both will be converted to public abstract by the compiler.
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20210101014702/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1017.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Choose the correct statement about the following code:

```java title=Example.java

1: publicinterfacePrintable {
2:   void fly();
3: }
4: interfaceArea {
5:   publicabstractObject getArea();
6: }
7: abstractclass Falcon implementsPrintable, Area {
8: }
```

- A. It compiles without issue.
- B. The code will not compile because of line 2.
- C. The code will not compile because of line 4.
- D. The code will not compile because of line 5.
- E. The code will not compile because of lines 2 and 5.
- F. The code will not compile because the class Falcon doesn't implement the interface methods.

```java title=Example.java
A.
```

## Note

Although the definition of methods on lines 2 and 5 vary, both will be converted to public abstract by the compiler.

Line 4 is fine, because an interface can have public or default access.

Finally, the class Falcon doesn't need to implement the interface methods because it is marked as abstract.

Therefore, the code will compile without issue.

PreviousNext

## Related

- Java OCA OCP Practice Question 1014
- Java OCA OCP Practice Question 1015
- Java OCA OCP Practice Question 1016
- Java OCA OCP Practice Question 1018
- Java OCA OCP Practice Question 1019
