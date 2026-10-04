---
title: Java OCA OCP Practice Question 1
nav: Java OCA OCP Practice Ques...
description: When does the string created on line 2 become eligible for garbage collection?
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20210101014421/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1.html
---
## Question

When does the string created on line 2 become eligible for garbage collection?

```java title=Example.java

1. String s = "aaa";
2. String t = newString(s);
3. t += "zzz";
4. t = t.substring(0);
5. t = null;
```

- A. After line 3
- B. After line 4
- C. After line 5
- D. The string created on line 2 does not become eligible for garbage collection in this code.

```java title=Example.java
A.
```

## Note

Line 3 creates a new string that contains aaazzz and assigns t to point to that new string.

At that moment there are no references to the string created on line 2 ( "aaa"), so it becomes eligible for garbage collection.

PreviousNext

## Related

- Java text file read by FileChannel
- Java text file read line by line
- Java text file replace text
- Java OCA OCP Practice Question 2
- Java OCA OCP Practice Question 3
