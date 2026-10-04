---
title: Java OCA OCP Practice Question 116
nav: Java OCA OCP Practice Ques...
description: Every enum comes with a static values() method that returns an array of the enum's values, in the order in which they are declared in the enum.
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20210101014439/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-116.html
---
## Question

Given:

```java title=Example.java

3. publicclass Main {
4.   publicenum Days { MON, TUE, WED };
5.   publicstaticvoid main(String[] args) {
6.     for(Days d : Days.values() )
7.       ;
8.     Days [] d2 = Days.values();
9.     System.out.println(d2[2]);
10.   }
11. }
```

What is the result?

Choose all that apply.

- A. TUE
- B. WED
- C. The output is unpredictable
- D. Compilation fails due to an error on line 4
- E. Compilation fails due to an error on line 6
- F. Compilation fails due to an error on line 8
- G. Compilation fails due to an error on line 9

```java title=Example.java
B is correct.
```

## Note

Every enum comes with a static values() method that returns an array of the enum's values, in the order in which they are declared in the enum.

A, C, D, E, F, and G are incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 113
- Java OCA OCP Practice Question 114
- Java OCA OCP Practice Question 115
- Java OCA OCP Practice Question 117
- Java OCA OCP Practice Question 118
