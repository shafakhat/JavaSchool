---
title: Java OCA OCP Practice Question 1136
nav: Java OCA OCP Practice Ques...
description: It initializes two variables and uses both variables in the condition check and the update statements.
section: Imported - java2s Archive
order: 1109
source: https://web.archive.org/web/20210101014722/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1136.html
---
## Question

What is the result of the following?

```java title=Example.java
String[] s = newString[] { "A", "B", "C" };
String[] times = newString[] { "Day", "Night" };
for (int i = 0, j = 0; i < s.length
        && j < times.length; i++, j++)
{
        System.out.print(s[i] + " " + times[j] + "-");
}
```

- A. A Day-
- B. A Day-B Night-
- C. The code does not compile.
- D. The code compiles but throws an exception at runtime.

```java title=Example.java
B.
```

## Note

This code is correct.

It initializes two variables and uses both variables in the condition check and the update statements.

Since it checks the size of both arrays correctly, it prints the first two sets of elements, and Option B is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1133
- Java OCA OCP Practice Question 1134
- Java OCA OCP Practice Question 1135
- Java OCA OCP Practice Question 1137
- Java OCA OCP Practice Question 1138
