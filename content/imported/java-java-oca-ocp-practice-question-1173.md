---
title: Java OCA OCP Practice Question 1173
nav: Java OCA OCP Practice Ques...
description: A Java programmer has written the following method that takes an array of integers and sums up all the integers that are less than 100.
section: Imported - java2s Archive
order: 1138
source: https://web.archive.org/web/20210101014728/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1173.html
---
## Question

A Java programmer has written the following method that takes an array of integers and sums up all the integers that are less than 100.

```java title=Example.java
publicclass Main {
   publicstaticvoid processArray(int[] values) {
      int sum = 0;
      int i = 0;try {
         while (values[i] < 100) {
            sum = sum + values[i];
            i++;
         }
      } catch (Exception e) {
      }
      System.out.println("sum = " + sum);
   }
   publicstaticvoid main(String args[]) {
      int[] a = { 1, 2, 3, 4, 5 };
      processArray(a);
   }
}
```

Which of the following are best practices to improve this code?

Select 2 options

- A. Use ArrayIndexOutOfBoundsException for the catch argument.
- B. Use ArrayIndexOutOfBoundsException for the catch argument and add code in the catch block to log or print the exception.
- C. Add code in the catch block to handle the exception.
- D. Use flow control to terminate the loop.

```java title=Example.java
Correct Options are  : B D
```

## Note

Empty catch blocks are a bad practice.

At run time, if the exception is thrown, the program will not show any sign of the exception.

PreviousNext

## Related

- Java OCA OCP Practice Question 1170
- Java OCA OCP Practice Question 1171
- Java OCA OCP Practice Question 1172
- Java OCA OCP Practice Question 1174
- Java OCA OCP Practice Question 1175
