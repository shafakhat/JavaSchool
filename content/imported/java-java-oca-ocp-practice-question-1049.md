---
title: Java OCA OCP Practice Question 1049
nav: Java OCA OCP Practice Ques...
description: Both static initializers are executed before main() is executed.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1049.html
---
## Question

What is the output of the following program?

```java title=Example.java
public class Main {
   static int i = 1;
   static {
      ++i;
   }
   public static void main(String[] args) {
      increment(i, 5);
      display(i);
   }
   static void increment(int n, int m) {
      n += m;
   }
   static void display(int n) {
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
