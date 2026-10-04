---
title: Java OCA OCP Practice Question 104
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 104
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20210101014437/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-104.html
---
## Question

Given:

```java title=Example.java
class Animal { privatevoid fly() {
     System.out.print("bang ");
  }
}
publicclass Bird extends Animal {
  publicstaticvoid main(String[] args) {
    new Bird().go();
  }
  void go() {
    fly();
    // Animal.fly();  // line A
  }
  privatevoid fly() { System.out.print("sh-bang "); }
}
```

Which are true? (Choose all that apply.)

- A. The output is bang
- B. The output is sh-bang
- C. Compilation fails.
- D. If line A is uncommented, the output is bang bang
- E. If line A is uncommented, the output is sh-bang bang
- F. If line A is uncommented, compilation fails.

```java title=Example.java
B and F are correct.
```

## Note

Since Animal.fly() is private, it can't be overridden.

It is invisible to class Bird.

A, C, D, and E are incorrect based on the above.

PreviousNext

## Related

- Java OCA OCP Practice Question 101
- Java OCA OCP Practice Question 102
- Java OCA OCP Practice Question 103
- Java OCA OCP Practice Question 105
- Java OCA OCP Practice Question 106
