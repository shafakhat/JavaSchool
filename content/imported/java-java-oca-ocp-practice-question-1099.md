---
title: Java OCA OCP Practice Question 1099
nav: Java OCA OCP Practice Ques...
description: How many of the loop types (while, do while, traditional for, and enhanced for) allow you to write code that creates an infinite loop?
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20210101014716/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1099.html
---
## Question

How many of the loop types (while, do while, traditional for, and enhanced for) allow you to write code that creates an infinite loop?

- A. One
- B. Two
- C. Three
- D. Four

```java title=Example.java
C.
```

## Note

It is not possible to create an infinite loop using a for-each because it simply loops through an array or ArrayList.

The other types allow infinite loops, such as, for example, do { } while(true), for(;;) and while(true).

Option C is correct.

It is possible to create an infinite loop with for-each by creating your own custom Iterable.

PreviousNext

## Related

- Java OCA OCP Practice Question 1096
- Java OCA OCP Practice Question 1097
- Java OCA OCP Practice Question 1098
- Java OCA OCP Practice Question 1100
- Java OCA OCP Practice Question 1101
