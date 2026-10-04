---
title: Java OCA OCP Practice Question 1063
nav: Java OCA OCP Practice Ques...
description: Line 6 catches the exception, line 7 prints Problem, and then line 8 calls System.exit, which terminates the JVM.
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1063.html
---
## Question

What is the output of the following program?

```java title=Example.java
1: publicclass Main {
2:   publicvoid start() {
3:    try {
4:      System.out.print("Starting up ");
5:      thrownewException();
6:    } catch (Exception e) {
7:       System.out.print("Problem ");
8:       System.exit(0);
9:    } finally {
10:      System.out.print("Shutting down ");
11:   }
12:  }
13:  publicstaticvoid main(String[] args) {
14:    new Main().start();
15:  }
16:}
```

- A. Starting up
- B. Starting up Problem
- C. Starting up Problem Shutting down
- D. Starting up Shutting down
- E. The code does not compile.
- F. An uncaught exception is thrown.

```java title=Example.java
B.
```

## Note

The main() method invokes start on a new Main object.

Line 4 prints Starting up; then line 5 throws an Exception.

Line 6 catches the exception, line 7 prints Problem, and then line 8 calls System.exit, which terminates the JVM.

The finally block does not execute because the JVM is no longer running.

PreviousNext

## Related

- Java OCA OCP Practice Question 1060
- Java OCA OCP Practice Question 1061
- Java OCA OCP Practice Question 1062
- Java OCA OCP Practice Question 1064
- Java OCA OCP Practice Question 1065
