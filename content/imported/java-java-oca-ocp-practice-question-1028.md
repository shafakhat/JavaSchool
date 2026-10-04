---
title: Java OCA OCP Practice Question 1028
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 1028
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1028.html
---
## Question

What is the output of the following program?

```java title=Example.java
publicclass Main {
   staticint i = 1, j = 2;
   static {
      display(i);
   }
   publicstaticvoid main(String[] args) {
      display(j);
   }
   staticvoid display(int n) {
      System.out.print(n);
   }
}
```

- A. 1
- B. 2
- C. 12
- D. 21

```java title=Example.java
C.
```

## Note

The static initializer is executed followed by main().

PreviousNext

## Related

- Java OCA OCP Practice Question 1025
- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1029
- Java OCA OCP Practice Question 1030
