---
title: Java OCA OCP Practice Question 1072
nav: Java OCA OCP Practice Ques...
description: main() doesn't catch the exception either, so the program terminates and the stack trace for the NumberFormatException is printed.
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20210101014711/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1072.html
---
## Question

What is the output of the following program?

```java title=Example.java

1:  publicclass Main {
2:    publicString name;
3:    publicvoid parseName() {
4:      System.out.print("1");
5:      try { /*www.java2s.com*/
6:        System.out.print("2");
7:        int x = Integer.parseInt(name);
8:        System.out.print("3");
9:      } catch (NullPointerException e) {
10:       System.out.print("4");
11:     }
12:     System.out.print("5");
13:   }
14:   publicstaticvoid main(String[] args) {
15:     Main m = new Main();
16:     m.name = "Leo";
17:     m.parseName();
18:     System.out.print("6");
19:   }
20: }
```

- A. 12, followed by a stack trace for a NumberFormatException
- B. 124, followed by a stack trace for a NumberFormatException
- C. 12456
- D. 12456
- E. 1256, followed by a stack trace for a NumberFormatException
- F. The code does not compile.
- G. An uncaught exception is thrown.

```java title=Example.java
A.
```

## Note

The parseName method is invoked on a new Main object.

Line 4 prints 1.

The try block is entered, and line 6 prints 2.

Line 7 throws a NumberFormatException.

It isn't caught, so parseName ends.

main() doesn't catch the exception either, so the program terminates and the stack trace for the NumberFormatException is printed.

PreviousNext

## Related

- Java OCA OCP Practice Question 1069
- Java OCA OCP Practice Question 1070
- Java OCA OCP Practice Question 1071
- Java OCA OCP Practice Question 1073
- Java OCA OCP Practice Question 1074
