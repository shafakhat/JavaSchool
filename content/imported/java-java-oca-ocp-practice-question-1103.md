---
title: Java OCA OCP Practice Question 1103
nav: Java OCA OCP Practice Ques...
description: Braces are optional around loops if there is only one statement.
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20210101014716/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1103.html
---
## Question

What happens when running the following code?

```java title=Example.java
do (
   System.out.println("aaa");
) while (false);
```

- A. It completes successfully without output.
- B. It outputs helium once.
- C. It keeps outputting helium.
- D. The code does not compile.

```java title=Example.java
D.
```

## Note

Braces are optional around loops if there is only one statement.

Parentheses are not allowed to surround a loop body though, so the code does not compile, and Option D is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1100
- Java OCA OCP Practice Question 1101
- Java OCA OCP Practice Question 1102
- Java OCA OCP Practice Question 1104
- Java OCA OCP Practice Question 1105
