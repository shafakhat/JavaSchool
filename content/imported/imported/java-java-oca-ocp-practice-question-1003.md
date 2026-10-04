---
title: Java OCA OCP Practice Question 1003
nav: Java OCA OCP Practice Ques...
description: Commas are used to separate statements within the initialization and iteration parts of a for statement.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20210101014700/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1003.html
---
## Question

What is wrong with the following for statement?

```java title=Example.java
for(i=0; j=0, i<10; ++i, j += i) {
    k += i*i + j*j;
}
```

- A. It should include more than one statement in the statement block.
- B. There should be a comma between i=0 and j=0.
- C. It uses more than one loop index.
- D. There should be a semicolon between j=0 and i<10.

```java title=Example.java
B and D.
```

## Note

Commas are used to separate statements within the initialization and iteration parts of a for statement.

Semicolons are used to separate the initialization, loop condition, and iteration parts of the for statement.

PreviousNext

## Related

- Java OCA OCP Practice Question 1000
- Java OCA OCP Practice Question 1001
- Java OCA OCP Practice Question 1002
- Java OCA OCP Practice Question 1004
- Java OCA OCP Practice Question 1005
