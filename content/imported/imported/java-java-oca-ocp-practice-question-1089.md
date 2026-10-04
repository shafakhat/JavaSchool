---
title: Java OCA OCP Practice Question 1089
nav: Java OCA OCP Practice Ques...
description: Immediately after v is initialized, the loop condition is checked.
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20210101014714/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1089.html
---
## Question

What does the following code output?

```java title=Example.java
String v = "";
while (v.length() != 2)
        v+="a";
System.out.println(v);
```

- A. aa
- B. aaa
- C. The loops complete with no output.
- D. This is an infinite loop.

```java title=Example.java
A.
```

## Note

Immediately after v is initialized, the loop condition is checked.

The variable v is of length 0, which is not equal to 2 so the loop is entered.

In the loop body, v becomes length 1 with contents "a".

The loop index is checked again and now 1 is not equal to 2.

The loop is entered and v becomes length 2 and contains "aa".

Then the loop index is checked again.

Since the length is now 2, the loop is completed and aa is output.

Option A is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1086
- Java OCA OCP Practice Question 1087
- Java OCA OCP Practice Question 1088
- Java OCA OCP Practice Question 1090
- Java OCA OCP Practice Question 1091
