---
title: Java OCA OCP Practice Question 112
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 112
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20210101014438/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-112.html
---
## Question

Given:

```java title=Example.java

1. publicclass Task implements Actionable
     { publicvoid doIt() { } }
2. /*www.java2s.com*/
3. abstractclass Test extends Task { }
4.
5. abstractclass Compile extends Task
     { publicvoid doIt(int x) { } }
6.
7. class Run extends Task implements Actionable
     { publicvoid doStuff() { } }
8.
9. interface Actionable { publicvoid doIt(); }
```

What is the result? (Choose all that apply.)

- A. Compilation succeeds
- B. Compilation fails with an error on line 1
- C. Compilation fails with an error on line 3
- D. Compilation fails with an error on line 5
- E. Compilation fails with an error on line 7
- F. Compilation fails with an error on line 9

```java title=Example.java
A is correct; all of these are legal declarations.
```

## Note

B, C, D, E, and F are incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 109
- Java OCA OCP Practice Question 110
- Java OCA OCP Practice Question 111
- Java OCA OCP Practice Question 113
- Java OCA OCP Practice Question 114
