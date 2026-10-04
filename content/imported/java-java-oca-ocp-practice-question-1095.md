---
title: Java OCA OCP Practice Question 1095
nav: Java OCA OCP Practice Ques...
description: It is not in scope after the loop where it is referenced by the println().
section: Imported - java2s Archive
order: 1074
source: https://web.archive.org/web/20210101014715/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1095.html
---
## Question

What is the result of the following code?

```java title=Example.java
do {
        int count = 0;
        do {
           count++;
        } while (count < 2);
           break;
} while (true);
System.out.println(count);
```

- A. 2
- B. 3
- C. The code does not compile.
- D. This is an infinite loop.

```java title=Example.java
C.
```

## Note

At first this code appears to be an infinite loop.

The count variable is declared inside the loop.

It is not in scope after the loop where it is referenced by the println().

The code does not compile, and Option C is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1092
- Java OCA OCP Practice Question 1093
- Java OCA OCP Practice Question 1094
- Java OCA OCP Practice Question 1096
- Java OCA OCP Practice Question 1097
