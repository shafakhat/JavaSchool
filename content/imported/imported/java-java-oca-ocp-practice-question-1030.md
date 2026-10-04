---
title: Java OCA OCP Practice Question 1030
nav: Java OCA OCP Practice Ques...
description: What should be inserted in the code given below at line marked // 10:
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1030.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What should be inserted in the code given below at line marked // 10:

```java title=Example.java
class MyClass{
}

class MyComparable implementsComparable<MyClass>{
   publicint compareTo (  *INSERT CODE HERE*  x ){ //10 return 0;
    }
}
```

Select 1 option

- A. Object
- B. MyClass
- C. Object<MyClass>
- D. Comparable<MyClass>
- E. Comparable

```java title=Example.java
Correct Option is  : B
```

## Note

Since MyComparable class specifies that it implements the Comparable interface that has been typed to MyClass, it must implement compareTo() method that takes a MyClass.

Had it not declared a typed Comparable in its implements clause, compareTo(Object x) would have been correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1029
- Java OCA OCP Practice Question 1031
- Java OCA OCP Practice Question 1032
