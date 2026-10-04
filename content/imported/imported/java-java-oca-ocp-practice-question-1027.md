---
title: Java OCA OCP Practice Question 1027
nav: Java OCA OCP Practice Ques...
description: Option B is incorrect, since an abstract class could implement Printable without the need to override the print() method.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1027.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Which statements are true about the following code?

Choose all that apply

```java title=Example.java

1: interfacePrintable {
2:   publicabstractvoid print();
3: }
4: publicinterface Writable extendsPrintable {
5:   publicvoid write();
6: }
```

- A. The Writable interface doesn't compile.
- B. A class that implements Printable must override the print() method.
- C. A class that implements Writable inherits both the print() and write() methods.
- D. A class that implements Writable only inherits the write() method.
- E. An interface cannot extend another interface.

```java title=Example.java
C.
```

## Note

The code compiles without issue, so option A is wrong.

Option B is incorrect, since an abstract class could implement Printable without the need to override the print() method.

Option C is correct; any class that implements Writable automatically inherits its methods, as well as any inherited methods defined in the parent interface. Because option C is correct, it follows that option D is incorrect.

Finally, an interface can extend multiple interfaces, so option E is incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1025
- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1029
