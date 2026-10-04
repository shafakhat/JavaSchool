---
title: Java OCA OCP Practice Question 1058
nav: Java OCA OCP Practice Ques...
description: What is printed besides the stack trace caused by the NullPointerException from line 16?
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1058.html
---
## Question

What is printed besides the stack trace caused by the NullPointerException from line 16?

```java title=Example.java

1: publicclass Main {
2:   publicvoid go() {
3:     System.out.print("A");
4:     try { //www.java2s.com
5:         stop();
6:     } catch (ArithmeticException e) {
7:         System.out.print("B");
8:     } finally {
9:         System.out.print("C");
10:    }
11:    System.out.print("D");
12:  }
13:  publicvoid stop() {
14:    System.out.print("E");
15:    Object x = null;
16:    x.toString();
17:    System.out.print("F");
18:  }
19:  publicstaticvoid main(String[] args) {
20:    new Main().go();
21:  }
22: }
```

```java title=Example.java

A.  AE
B.  AEBCD
C.  AEC
D.  AECD
E.  No output appears other than the stack trace.
```

```java title=Example.java
C.
```

## Note

The main() method invokes go and A is printed on line 3.

The stop method is invoked and E is printed on line 14.

Line 16 throws a NullPointerException, so stop immediately ends and line 17 doesn't execute.

The exception isn't caught in go, so the go method ends as well, but not before its finally block executes and C is printed on line 9.

Because main() doesn't catch the exception, the stack trace displays and no further output occurs, so AEC was the output printed before the stack trace.

PreviousNext

## Related

- Java OCA OCP Practice Question 1055
- Java OCA OCP Practice Question 1056
- Java OCA OCP Practice Question 1057
- Java OCA OCP Practice Question 1059
- Java OCA OCP Practice Question 1060
