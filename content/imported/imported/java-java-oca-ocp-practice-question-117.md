---
title: Java OCA OCP Practice Question 117
nav: Java OCA OCP Practice Ques...
description: The two operands, which are originally bytes, are converted to ints before the multiplication.
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20210101014439/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-117.html
---
## Question

Will the following code compile?

```java title=Example.java

1. byte b = 2;
2. byte b1 = 3;
3. b = b * b1;
```

- A. Yes
- B. No

```java title=Example.java
B.
```

## Note

The code will fail to compile at line 3.

The two operands, which are originally bytes, are converted to ints before the multiplication.

The result of the multiplication is an int, which cannot be assigned to byte b.

PreviousNext

## Related

- Java OCA OCP Practice Question 114
- Java OCA OCP Practice Question 115
- Java OCA OCP Practice Question 116
- Java OCA OCP Practice Question 118
- Java OCA OCP Practice Question 119
