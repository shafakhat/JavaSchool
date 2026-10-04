---
title: Java OCA OCP Practice Question 1066
nav: Java OCA OCP Practice Ques...
description: The parseName() method is invoked within main() on a new Main object.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20210101014710/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1066.html
---
## Question

What is the output of the following program?

```java title=Example.java
1:  publicclass Main {
2:    publicString name;
3:    publicvoid parseName() {
4:      System.out.print("1");
5:      try {
6:        System.out.print("2");
7:        int x = Integer.parseInt(name);
8:        System.out.print("3");
9:      } catch (NumberFormatException e) {
10:       System.out.print("4");
11:     }
12:   }
13:   publicstaticvoid main(String[] args) {
14:     Main m = new Main();
15:     m.name = "Leroy";
16:     m.parseName();
17:     System.out.print("5");
18:   }
19:}
```

- A. 12
- B. 1234
- C. 1235
- D. 124
- E. 1245
- F. The code does not compile.
- G. An uncaught exception is thrown.

```java title=Example.java
E.
```

## Note

The parseName() method is invoked within main() on a new Main object.

Line 4 prints 1.

The try block executes and 2 is printed.

Line 7 throws a NumberFormatException, so line 8 doesn't execute.

The exception is caught on line 9, and line 10 prints 4.

Because the exception is handled, execution resumes normally.

parseName runs to completion, and line 17 executes, printing 5.

That's the end of the program, so the output is 1245.

PreviousNext

## Related

- Java OCA OCP Practice Question 1063
- Java OCA OCP Practice Question 1064
- Java OCA OCP Practice Question 1065
- Java OCA OCP Practice Question 1067
- Java OCA OCP Practice Question 1068
