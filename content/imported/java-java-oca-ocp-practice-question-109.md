---
title: Java OCA OCP Practice Question 109
nav: Java OCA OCP Practice Ques...
description: What is the result of compiling and executing the following application?
section: Imported - java2s Archive
order: 1071
source: https://web.archive.org/web/20210101014438/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-109.html
---
## Question

What is the result of compiling and executing the following application?

```java title=Example.java
package mypkg;
publicclass MyClass {
        privatestaticboolean heatWave = true;
        publicstaticvoid main() {
           boolean heatWave = false;
           System.out.print(heatWave);
        }
}
```

- A. true
- B. false
- C. It does not compile.
- D. It compiles but throws an error at runtime.

```java title=Example.java
D.
```

## Note

The application compiles without issue, Option C is incorrect.

The application does not execute, since the main() method does not have the correct method signature.

It is missing the required input argument, an array of String.

Trying to execute the application without a proper entry point produces an error.

Option D is the correct answer.

PreviousNext

## Related

- Java OCA OCP Practice Question 106
- Java OCA OCP Practice Question 107
- Java OCA OCP Practice Question 108
- Java OCA OCP Practice Question 110
- Java OCA OCP Practice Question 111
