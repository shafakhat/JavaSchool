---
title: Java OCA OCP Practice Question 11
nav: Java OCA OCP Practice Ques...
description: The Runnable interface defines a run() method with void return type and no parameters.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-11.html
---
## Question

Which one statement is true for the following code?

```java title=Example.java
 1. class MyList extends java.util.Vector
 2.   implements Runnable {
 3.     public void run(String message) {
 4.       System.out.println("in run() method: " +
 5.       message);
 6.   }
 7. }
 8.
 9. class MyListTest {
10.   public static void main(String args[]) {
12.     MyList g = new MyList();
13.     Thread t = new Thread(g);
14.     t.start();
15.   }
16. }
```

- A. Compiler error, because class MyList does not correctly implement the Runnable interface.
- B. Compiler error at line 13, because you cannot pass a parameter to the constructor of a Thread.
- C. Compile correctly but will crash with an exception at line 13.
- D. Compile correctly but will crash with an exception at line 14.
- E. Compile correctly and will execute without throwing any exceptions.

```java title=Example.java
A.
```

## Note

The Runnable interface defines a run() method with void return type and no parameters.

The method given in the problem has a String parameter, so the compiler will complain that class MyList does not define void run() from interface Runnable.

B is wrong, because you can pass a parameter to a thread's constructor; the parameter becomes the thread's target.

C, D, and E are wrong.

PreviousNext

## Related

- Java OCA OCP Practice Question 8
- Java OCA OCP Practice Question 9
- Java OCA OCP Practice Question 10
- Java OCA OCP Practice Question 12
- Java OCA OCP Practice Question 13
