---
title: Java OCA OCP Practice Question 1086
nav: Java OCA OCP Practice Ques...
description: Which of the following can be inserted on line 8 to make this code compile?
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1086.html
---
## Question

Which of the following can be inserted on line 8 to make this code compile?

Choose all that apply

```java title=Example.java
7: public void r() throws IOException {
8:   // INSERT CODE HERE
9: }
```

- A. System.out.println("it's ok");
- B. throw new Exception() ;
- C. throw new IllegalArgumentException() ;
- D. throw new java.io. IOException() ;
- E. throw new RuntimeException() ;

```java title=Example.java
A, C, D, E.
```

## Note

A method that declares an exception isn't required to throw one, making option A correct.

Runtime exceptions can be thrown in any method, making options C and E correct.

Option D matches the exception type declared and so is also correct.

Option B is incorrect because a broader exception is not allowed.

PreviousNext

## Related

- Java OCA OCP Practice Question 1083
- Java OCA OCP Practice Question 1084
- Java OCA OCP Practice Question 1085
- Java OCA OCP Practice Question 1087
- Java OCA OCP Practice Question 1088
