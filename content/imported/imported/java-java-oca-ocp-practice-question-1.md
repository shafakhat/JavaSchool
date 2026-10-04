---
title: Java OCA OCP Practice Question 1
nav: Java OCA OCP Practice Ques...
description: When does the string created on line 2 become eligible for garbage collection?
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20210101014421/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

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
