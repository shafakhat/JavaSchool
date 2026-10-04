---
title: Java OCA OCP Practice Question 1079
nav: Java OCA OCP Practice Ques...
description: Which of the following types is objects not allowed to be in order for this code to compile?
section: Imported - java2s Archive
order: 1059
source: https://web.archive.org/web/20210101014712/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1079.html
---
## Question

Which of the following types is objects not allowed to be in order for this code to compile?

```java title=Example.java
for (Object obj : objects) {
}
```

- A. ArrayList<Integer>
- B. int[]
- C. StringBuilder
- D. All of these are allowed.

```java title=Example.java
C.
```

## Note

A for-each loop is allowed to be used with arrays and ArrayList objects.

StringBuilder is not an allowed type for this loop, so Option C is the answer.

PreviousNext

## Related

- Java OCA OCP Practice Question 1076
- Java OCA OCP Practice Question 1077
- Java OCA OCP Practice Question 1078
- Java OCA OCP Practice Question 1080
- Java OCA OCP Practice Question 1081
