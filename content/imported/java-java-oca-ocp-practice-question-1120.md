---
title: Java OCA OCP Practice Question 1120
nav: Java OCA OCP Practice Ques...
description: An array is declared by using curly braces {} instead of square brackets [].
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20210101014719/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1120.html
---
## Question

Given the following code, what is the expected outcome?

```java title=Example.java
publicclass Test {
      publicstaticvoid main(String [] a) {
         int [] b = [1,2,3,4];
         System.out.println("a[2]=" + a[2]);
      }
}
```

- A. The code compiles but does not output anything.
- B. "a[2]=3" is printed out to the console.
- C. "a[2]=2" is printed out to the console.
- D. The code does not compile.
- E. None of the above.

```java title=Example.java
D.
```

## Note

The declaration of the integer array is incorrect.

An array is declared by using curly braces {} instead of square brackets [].

PreviousNext

## Related

- Java OCA OCP Practice Question 1117
- Java OCA OCP Practice Question 1118
- Java OCA OCP Practice Question 1119
- Java OCA OCP Practice Question 1121
- Java OCA OCP Practice Question 1122
