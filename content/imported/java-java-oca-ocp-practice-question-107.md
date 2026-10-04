---
title: Java OCA OCP Practice Question 107
nav: Java OCA OCP Practice Ques...
description: The hash code contract states that if two objects are equal, they must have equal hash codes.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20210101014438/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-107.html
---
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
    }
D.  publicint hashCode() {
          return a*b;
    }
E.  publicint hashCode() {
          return (int)Math.random();
    }
java title=Example.java
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
