---
title: Java OCA OCP Practice Question 107
nav: Java OCA OCP Practice Ques...
description: The hash code contract states that if two objects are equal, they must have equal hash codes.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20210101014438/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-107.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Given the following class:

```java title=Example.java
class MyClass {
     int a, b;

     publicboolean equals(Object x) {
       MyClass that = (MyClass)x;
       returnthis.a == that.a;
     }
}
```

Which methods below honor the hash code contract?

```java title=Example.java

A.  publicint hashCode() { return a; }

B.  publicint hashCode() { return b; }

C.  publicint hashCode() {
          return a+b;
    } /*fromwww.java2s.com*/

D.  publicint hashCode() {
          return a*b;
    }

E.  publicint hashCode() {
          return (int)Math.random();
    }
```

```java title=Example.java
A, E.
```

## Note

The hash code contract states that if two objects are equal, they must have equal hash codes.

In this case two objects are equal if their a values are equal.

If two such objects have different b values, then answers B, C, and D will return unequal hash codes for equal objects, which violates the contract.

E always returns 0; it's strange and inefficient, but it doesn't violate the contract.

PreviousNext

## Related

- Java OCA OCP Practice Question 104
- Java OCA OCP Practice Question 105
- Java OCA OCP Practice Question 106
- Java OCA OCP Practice Question 108
- Java OCA OCP Practice Question 109
