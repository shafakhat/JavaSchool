---
title: Java OCA OCP Practice Question 110
nav: Java OCA OCP Practice Ques...
description: Variable a has default access, so it cannot be accessed from outside the package.
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20210101014438/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-110.html
---
## Question

Given two files:

```java title=Example.java
1. package pkgA;
2. publicclass Foo {
3.    int a = 5;
4.    protectedint b = 6;
5.    publicint c = 7;
6. }
3. package pkgB;
4. import pkgA.*;
5. publicclass Baz {
6.   publicstaticvoid main(String[] args) {
7.     Foo f = new Foo();
8.     System.out.print(" " + f.a);
9.     System.out.print(" " + f.b);
10.     System.out.println(" " + f.c);
11.   }
12. }
```

What is the result?

Choose all that apply.

- A. 5 6 7
- B. 5 followed by an exception
- C. Compilation fails with an error on line 7
- D. Compilation fails with an error on line 8
- E. Compilation fails with an error on line 9
- F. Compilation fails with an error on line 10

```java title=Example.java
D and E are correct.
```

## Note

Variable a has default access, so it cannot be accessed from outside the package.

Variable b has protected access in pkgA.

A, B, C, and F are incorrect based on the above information.

PreviousNext

## Related

- Java OCA OCP Practice Question 107
- Java OCA OCP Practice Question 108
- Java OCA OCP Practice Question 109
- Java OCA OCP Practice Question 111
- Java OCA OCP Practice Question 112
