---
title: Java OCA OCP Practice Question 1077
nav: Java OCA OCP Practice Ques...
description: On the first iteration of the loop, the if statement executes and prints inflate-.
section: Imported - java2s Archive
order: 1057
source: https://web.archive.org/web/20210101014712/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1077.html
---
## Question

What is the output of the following?

```java title=Example.java
publicclass Main {
   publicstaticvoid main(String[] args) {
      boolean v = false;
      do {//fromwww.java2s.comif (!v) {
            v = true;
            System.out.print("inflate-");
         }
      } while (!v);
      System.out.println("done");

   }
}
```

- A. done
- B. inflate-done
- C. The code does not compile.
- D. This is an infinite loop.

```java title=Example.java
B.
```

## Note

This is a correct do-while loop.

On the first iteration of the loop, the if statement executes and prints inflate-.

Then the loop condition is checked.

The variable v is true, so the loop condition is false and the loop completes.

PreviousNext

## Related

- Java OCA OCP Practice Question 1074
- Java OCA OCP Practice Question 1075
- Java OCA OCP Practice Question 1076
- Java OCA OCP Practice Question 1078
- Java OCA OCP Practice Question 1079
