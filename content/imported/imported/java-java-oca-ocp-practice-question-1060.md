---
title: Java OCA OCP Practice Question 1060
nav: Java OCA OCP Practice Ques...
description: What is the output of the following snippet, assuming a and b are both 0?
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1060.html
---
## Question

What is the output of the following snippet, assuming a and b are both 0?

```java title=Example.java

3:     try {
4:       return a / b;
5:     } catch (RuntimeException e) {
6:       return -1;
7:     } catch (ArithmeticException e) {
8:       return 0;
9:     } finally {
10:      System.out.print("done");
11:    }
```

- A. -1
- B. 0
- C. done-1
- D. done0
- E. The code does not compile.
- F. An uncaught exception is thrown.

```java title=Example.java
E.
```

## Note

The order of catch blocks is important because they're checked in the order they appear after the try block.

Because ArithmeticException is a child class of RuntimeException, the catch block on line 7 is unreachable.

If an ArithmeticException is thrown in try try block, it will be caught on line 5.

Line 7 generates a compiler error because it is unreachable code.

PreviousNext

## Related

- Java OCA OCP Practice Question 1057
- Java OCA OCP Practice Question 1058
- Java OCA OCP Practice Question 1059
- Java OCA OCP Practice Question 1061
- Java OCA OCP Practice Question 1062
