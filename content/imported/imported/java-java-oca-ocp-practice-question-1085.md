---
title: Java OCA OCP Practice Question 1085
nav: Java OCA OCP Practice Ques...
description: This is a correct loop to go through an ArrayList or List starting from the end.
section: Imported - java2s Archive
order: 1066
source: https://web.archive.org/web/20210101014714/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1085.html
---
## Question

What does the following code output?

```java title=Example.java
List<String> v = Arrays.asList("can", "cup");
for (int c = v.size() - 1; c >= 0; c--)
       System.out.print(v.get(c) + ",");
```

- A. can,cup,
- B. cup,can,
- C. The code does not compile.
- D. None of the above

```java title=Example.java
B.
```

## Note

This is a correct loop to go through an ArrayList or List starting from the end.

It starts with the last index in the list and goes to the first index in the list.

Option B is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1082
- Java OCA OCP Practice Question 1083
- Java OCA OCP Practice Question 1084
- Java OCA OCP Practice Question 1086
- Java OCA OCP Practice Question 1087
