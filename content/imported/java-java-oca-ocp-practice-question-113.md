---
title: Java OCA OCP Practice Question 113
nav: Java OCA OCP Practice Ques...
description: MyRunnable implements java.lang.Runnable but does not extend Thread.
section: Imported - java2s Archive
order: 1105
source: https://web.archive.org/web/20210101014439/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-113.html
---
## Question

Suppose MyThread extends java.lang.Thread.

MyRunnable implements java.lang.Runnable but does not extend Thread.

Both classes have no-args constructors.

Which of the following cause a thread in the JVM to begin execution?

Choose all correct options.

```java title=Example.java
A.  (new MyThread()).start();
B.  (new MyThread()).run();
C.  (new MyRunnable()).run();
D.  (newThread(new MyRunnable()))
E.   .start();
java title=Example.java
A, D.
```

## Note

A is correct because the start() method of Thread causes a thread to begin execution of the thread object's run() method.

Calling run() directly as in B and C just causes the run() method to execute in the current thread.

D creates a new thread whose target is an instance of MyRunnable; this is the typical way to use the Runnable interface.

PreviousNext

## Related

- Java OCA OCP Practice Question 110
- Java OCA OCP Practice Question 111
- Java OCA OCP Practice Question 112
- Java OCA OCP Practice Question 114
- Java OCA OCP Practice Question 115
