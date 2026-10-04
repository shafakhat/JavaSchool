---
title: Java OCA OCP Practice Question 1049
nav: Java OCA OCP Practice Ques...
description: Both static initializers are executed before main() is executed.
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20210101014707/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1049.html
---
## Question

What is the output of the following program?

```java title=Example.java
publicclass Main {
   staticint i = 1;
   static {//fromwww.java2s.com
      ++i;
   }

   publicstaticvoid main(String[] args) {
      increment(i, 5);
      display(i);
   }

   staticvoid increment(int n, int m) {
      n += m;
   }

   staticvoid display(int n) {
      System.out.print(n);
   }

   static {
      ++i;
   }
}
```

- A. 1
- B. 3
- C. 6
- D. 7

```java title=Example.java
B.
```

## Note

Both static initializers are executed before main() is executed.

The increment() method has no effect on the value of i.

PreviousNext

## Related

- Java OCA OCP Practice Question 1046
- Java OCA OCP Practice Question 1047
- Java OCA OCP Practice Question 1048
- Java OCA OCP Practice Question 1050
- Java OCA OCP Practice Question 1051
