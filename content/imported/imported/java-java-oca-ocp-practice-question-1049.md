---
title: Java OCA OCP Practice Question 1049
nav: Java OCA OCP Practice Ques...
description: Both static initializers are executed before main() is executed.
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20210101014707/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1049.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following program?

```java title=Example.java
publicclass Main {
   staticint i = 1;
   static {//fromwww.java2s.com
      ++i;
   }

   publicstaticvoid main(String[] args) {
      increment(i, 5);
      display(i);
   }

   staticvoid increment(int n, int m) {
      n += m;
   }

   staticvoid display(int n) {
      System.out.print(n);
   }

   static {
      ++i;
   }
}
```

- A. 1
- B. 3
- C. 6
- D. 7

```java title=Example.java
B.
```

## Note

Both static initializers are executed before main() is executed.

The increment() method has no effect on the value of i.

PreviousNext

## Related

- Java OCA OCP Practice Question 1046
- Java OCA OCP Practice Question 1047
- Java OCA OCP Practice Question 1048
- Java OCA OCP Practice Question 1050
- Java OCA OCP Practice Question 1051
