---
title: Java OCA OCP Practice Question 1134
nav: Java OCA OCP Practice Ques...
description: Fill in the blank so this code compiles and does not cause an infinite loop.
section: Imported - java2s Archive
order: 1108
source: https://web.archive.org/web/20210101014721/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1134.html
---
## Question

Fill in the blank so this code compiles and does not cause an infinite loop.

```java title=Example.java
t: while (true) {
        f: while(true) {
            ______
        }
}
```

- A. break;
- B. break f;
- C. break t;
- D. None of the above

```java title=Example.java
C.
```

## Note

Option A breaks out of the inner loop, but the outer loop is still infinite.

Option B has the same problem.

Option C is correct because it breaks out of both loops.

PreviousNext

## Related

- Java OCA OCP Practice Question 1131
- Java OCA OCP Practice Question 1132
- Java OCA OCP Practice Question 1133
- Java OCA OCP Practice Question 1135
- Java OCA OCP Practice Question 1136
