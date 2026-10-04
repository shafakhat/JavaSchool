---
title: Java OCA OCP Practice Question 1132
nav: Java OCA OCP Practice Ques...
description: Then count is set to 2 on the next iteration of the inner loop.
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20210101014721/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1132.html
---
## Question

What is the result of the following code?

```java title=Example.java
6:   int count = 0;
7:   do {
8:      do {
9:         count++;
10:     } while (count < 2);
11:     break;
12:  } while (true);
13:  System.out.println(count);
```

- A. 2
- B. 3
- C. The code does not compile.
- D. This is an infinite loop.

```java title=Example.java
A.
```

## Note

At first this code appears to be an infinite loop.

However, there is a break statement.

On line 6, count is set to 0.

On line 9, it is changed to 1.

Then the condition on line 10 runs.

count is less than 2 so the inner loop continues.

Then count is set to 2 on the next iteration of the inner loop.

The loop condition on line 10 runs again and this time is false.

The inner loop is completed.

Then line 11 of the outer loop runs and sends execution to after the loop on line 13.

At this point count is still 2, so Option A is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1129
- Java OCA OCP Practice Question 1130
- Java OCA OCP Practice Question 1131
- Java OCA OCP Practice Question 1133
- Java OCA OCP Practice Question 1134
