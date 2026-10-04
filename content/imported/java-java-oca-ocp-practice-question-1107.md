---
title: Java OCA OCP Practice Question 1107
nav: Java OCA OCP Practice Ques...
description: A while loop checks the boolean condition before entering the loop.
section: Imported - java2s Archive
order: 1088
source: https://web.archive.org/web/20210101014717/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1107.html
---
## Question

What does the following code output?

```java title=Example.java
int v = 0;
while (v > 0)
   System.out.println(v++);
```

- A. 0
- B. The code does not compile.
- C. The loops completes with no output.
- D. This is an infinite loop.

```java title=Example.java
C.
```

## Note

A while loop checks the boolean condition before entering the loop.

In this code, that condition is false, so the loop body is never run.

No output is produced, and Option C is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1104
- Java OCA OCP Practice Question 1105
- Java OCA OCP Practice Question 1106
- Java OCA OCP Practice Question 1108
- Java OCA OCP Practice Question 1109
