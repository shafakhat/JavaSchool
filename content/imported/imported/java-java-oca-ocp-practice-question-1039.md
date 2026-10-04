---
title: Java OCA OCP Practice Question 1039
nav: Java OCA OCP Practice Ques...
description: Given the following two declarations, which of the options will compile?
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20210101014706/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1039.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Consider the following classes:

```java title=Example.java
class A  {
      publicint getCode (){ return 2;}
}

class MySubClass extends A  {
  publicvoid doStuff ()  {
   }
}
```

Given the following two declarations, which of the options will compile?

```java title=Example.java

A a = null;
MySubClass aa = null;
```

Select 4 options

```java title=Example.java

A. a =  (MySubClass)aa;
B. a = new MySubClass ();
C. aa = new A ();
D. aa =  (MySubClass) a;
E. aa = a;
F.  ((MySubClass)a).doStuff ();
```

```java title=Example.java
Correct Options are  : A B D F
```

## Note

a is declared as a reference of class A and therefore, at run time, it is possible for a to point to an object of class MySubClass because A is a super class of MySubClass.

Hence, the compiler will not complain.

Although if a does not point to an object of class MySubClass at run time, a ClassCastException will be thrown.

A cast is required because the compiler needs to be assured that at run time a will point to an object of class MySubClass.

Once you cast a to MySubClass, you can call methods defined in MySubClass.

Of course, if a does not point to an object of class MySubClass at runtime, a ClassCastException will be thrown.

PreviousNext

## Related

- Java OCA OCP Practice Question 1036
- Java OCA OCP Practice Question 1037
- Java OCA OCP Practice Question 1038
- Java OCA OCP Practice Question 1040
- Java OCA OCP Practice Question 1041
