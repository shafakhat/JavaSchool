---
title: Java OCA OCP Practice Question 1053
nav: Java OCA OCP Practice Ques...
description: Had it been k-->0, it would imply, first compare k with 0, and then decrement k.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20210101014708/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1053.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What will the following code print when compiled and run:

```java title=Example.java
publicclass Main  {
    publicstaticvoid main (String [] args){
        int k = 2;
        do{
            System.out.println (k);
        }while (--k>0);
     }
}
```

Select 1 option

```java title=Example.java

A.  1 //fromwww.java2s.com

B.  1
    0

C.  2
    1

D.  2
    1
    0

E. It will keeping printing numbers in an infinite loop.

F. It will not compile.
```

```java title=Example.java
Correct Option is  : C
```

## Note

--k>0 implies, decrement the value of k and then compare with 0.

The loop will only execute twice, printing 2 and 1.

Had it been k-->0, it would imply, first compare k with 0, and then decrement k.

The loop would execute thrice, printing 2, 1, and 0.

PreviousNext

## Related

- Java OCA OCP Practice Question 1050
- Java OCA OCP Practice Question 1051
- Java OCA OCP Practice Question 1052
- Java OCA OCP Practice Question 1054
- Java OCA OCP Practice Question 1055
