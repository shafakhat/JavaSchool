---
title: Java OCA OCP Practice Question 1119
nav: Java OCA OCP Practice Ques...
description: String[] s = newString[] { "Downtown", "Uptown", "Brooklyn" };
section: Imported - java2s Archive
order: 1095
source: https://web.archive.org/web/20210101014719/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1119.html
---
## Question

What is the result of the following?

```java title=Example.java
String[] s = newString[] { "Downtown", "Uptown", "Brooklyn" };
String[] times = newString[] { "Day", "Night" };
for (int i = 0, j = 0; i < s.length
        && j < times.length; i++; j++)
{
        System.out.print(s[i] + " " + times[j] + "-");
}
```

- A. Downtown Day-
- B. Downtown Day-Uptown Night-
- C. The code does not compile.
- D. The code compiles but throws an exception at runtime.

```java title=Example.java
C.
```

## Note

Multiple update expressions are separated with a comma rather than a semicolon.

This makes Option C correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1116
- Java OCA OCP Practice Question 1117
- Java OCA OCP Practice Question 1118
- Java OCA OCP Practice Question 1120
- Java OCA OCP Practice Question 1121
