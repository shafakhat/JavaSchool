---
title: Java OCA OCP Practice Question 10
nav: Java OCA OCP Practice Ques...
description: Which of the following may appear in a subclass of Fish named Tuna that is not in the mypkg package?
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20210101014422/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-10.html
---
## Question

Given the following class:

```java title=Example.java
package mypkg;
publicclass Fish {
     protectedint size;
     protectedvoid swim() { }
}
```

Which of the following may appear in a subclass of Fish named Tuna that is not in the mypkg package?

- A. void swim() { }
- B. public void swim() { }
- C. size = 12;
- D. (new Tuna() ).size = 12;

```java title=Example.java
B, C.
```

## Note

A is illegal because it attempts to override the swim() method with a more restricted access mode.

B overrides with a less-restricted access mode, which is legal.

C is legal because it accesses protected superclass data of the current instance.

D is illegal because it accesses protected superclass data of a different instance.

PreviousNext

## Related

- Java OCA OCP Practice Question 7
- Java OCA OCP Practice Question 8
- Java OCA OCP Practice Question 9
- Java OCA OCP Practice Question 11
- Java OCA OCP Practice Question 12
