---
title: Java OCA OCP Practice Question 1147
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 1147
section: Imported - java2s Archive
order: 1115
source: https://web.archive.org/web/20210101014723/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1147.html
---
## Question

What is the output of the following?

```java title=Example.java

12:  int v = 8;
13:  for: while (v > 7) {
14:     v++;
15:     do {
16:        v--;
17:     } while (v > 5);
18:     breakfor;
19:  }
20:  System.out.println(v);
```

- A. 5
- B. 8
- C. The code does not compile.
- D. The code compiles but throws an exception at runtime.

```java title=Example.java
C.
```

## Note

The label of the loop is trying to use the keyword for.

This is not allowed, so the code does not compile.

If the label was valid, Option A would be correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1144
- Java OCA OCP Practice Question 1145
- Java OCA OCP Practice Question 1146
- Java OCA OCP Practice Question 1148
- Java OCA OCP Practice Question 1149
