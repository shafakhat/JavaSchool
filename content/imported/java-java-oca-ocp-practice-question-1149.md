---
title: Java OCA OCP Practice Question 1149
nav: Java OCA OCP Practice Ques...
description: On the first iteration of the loop, the if statement executes printing v-.
section: Imported - java2s Archive
order: 1117
source: https://web.archive.org/web/20210101014724/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1149.html
---
## Question

What is the output of the following?

```java title=Example.java
boolean v = false;
do {
        if (!v) {
           v = true;
           System.out.print("v-");
        }
} while (v);
System.out.println("done");
```

- A. done
- B. v-done
- C. The code does not compile.
- D. This is an infinite loop.

```java title=Example.java
D.
```

## Note

On the first iteration of the loop, the if statement executes printing v-.

Then the loop condition is checked.

The variable v is true, so the loop condition is true and the loop continues.

The if statement no longer runs, but the variable never changes state again, so the loop doesn't end.

PreviousNext

## Related

- Java OCA OCP Practice Question 1146
- Java OCA OCP Practice Question 1147
- Java OCA OCP Practice Question 1148
- Java OCA OCP Practice Question 1150
- Java OCA OCP Practice Question 1151
