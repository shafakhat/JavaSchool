---
title: Java OCA OCP Practice Question 1042
nav: Java OCA OCP Practice Ques...
description: Using the order of precedence, the equation contained within the parentheses is evaluated first.
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20210101014706/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1042.html
---
## Question

What is the value of x after the following line is executed?

```java title=Example.java

x = 32 * (31 - 10 * 3);
```

- A. 32
- B. 31
- C. 3
- D. 704
- E. None of the above

```java title=Example.java
A.
```

## Note

Using the order of precedence, the equation contained within the parentheses is evaluated first.

Using the order of precedence within the parentheses, the multiplication is executed first (10 * 3 = 30) and then the subtraction (31 - 30 = 1).

Once this is completed, the final equation is executed as 32 * 1, which equals 32.

PreviousNext

## Related

- Java OCA OCP Practice Question 1039
- Java OCA OCP Practice Question 1040
- Java OCA OCP Practice Question 1041
- Java OCA OCP Practice Question 1043
- Java OCA OCP Practice Question 1044
