---
title: Java OCA OCP Practice Question 114
nav: Java OCA OCP Practice Ques...
description: Variable names cannot begin with a #, and an array declaration can't include a size without an instantiation.
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20210101014439/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-114.html
---
## Question

Given:

```java title=Example.java
4. class MyClass {
5.   publicstaticvoid main(String[] args) {
6.     for(int __x = 0; __x < 3; __x++) ;
7.     int #lb = 7;
8.     long [] x [5];
9.     Boolean []ba[];
10.   }
11. }
```

What is the result?

Choose all that apply.

- A. Compilation succeeds
- B. Compilation fails with an error on line 6
- C. Compilation fails with an error on line 7
- D. Compilation fails with an error on line 8
- E. Compilation fails with an error on line 9

```java title=Example.java
C and D are correct.
```

## Note

Variable names cannot begin with a #, and an array declaration can't include a size without an instantiation.

The rest of the code is valid.

A, B, and E are incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 111
- Java OCA OCP Practice Question 112
- Java OCA OCP Practice Question 113
- Java OCA OCP Practice Question 115
- Java OCA OCP Practice Question 116
