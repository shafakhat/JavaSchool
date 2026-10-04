---
title: Java OCA OCP Practice Question 1126
nav: Java OCA OCP Practice Ques...
description: However, we aren't asked about whether the code compiles as is.
section: Imported - java2s Archive
order: 1103
source: https://web.archive.org/web/20210101014720/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1126.html
---
## Question

The following code outputs a single letter x.

What happens if you remove lines 25 and 28?

```java title=Example.java
23:  String race = "";
24:  loop:
25:  do {
26:     race += "x";
27:     break loop;
28:  } while (true);
29:  System.out.println(race);
```

- A. It prints an empty string.
- B. It still outputs a single letter x.
- C. It no longer compiles.
- D. It becomes an infinite loop.

```java title=Example.java
C.
```

## Note

The code compiles as is.

However, we aren't asked about whether the code compiles as is.

Line 27 refers to a loop label.

While the label is still present, it no longer points to a loop.

This causes the code to not compile, and Option C is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1123
- Java OCA OCP Practice Question 1124
- Java OCA OCP Practice Question 1125
- Java OCA OCP Practice Question 1127
- Java OCA OCP Practice Question 1128
