---
title: Java OCA OCP Practice Question 1145
nav: Java OCA OCP Practice Ques...
description: The first time the loop condition is checked, the variable v is null.
section: Imported - java2s Archive
order: 1113
source: https://web.archive.org/web/20210101014723/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1145.html
---
## Question

What is the output of the following?

```java title=Example.java
publicclass Main {
    publicstaticvoid main(String[] args) {
         String v = null;
         while (v == null);
            v = "v";
            System.out.print(v);
    }
}
```

- A. null
- B. v
- C. vv
- D. None of the above

```java title=Example.java
D.
```

## Note

The first time the loop condition is checked, the variable v is null.

The loop body is empty due to the semicolon right after the condition.

The loop condition keeps running with no opportunity for v to be set.

This is an infinite loop, and Option D is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1142
- Java OCA OCP Practice Question 1143
- Java OCA OCP Practice Question 1144
- Java OCA OCP Practice Question 1146
- Java OCA OCP Practice Question 1147
