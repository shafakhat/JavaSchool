---
title: Java OCA OCP Practice Question 1094
nav: Java OCA OCP Practice Ques...
description: Which of the following can be inserted into Lion to make this code compile?
section: Imported - java2s Archive
order: 1073
source: https://web.archive.org/web/20210101014715/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1094.html
---
## Question

Which of the following can be inserted into Lion to make this code compile?

Choose all that apply

```java title=Example.java
class Ex1 extendsException {}
class Ex2 extendsRuntimeException {}
interface Roar {
 void roar() throws Ex1;
}
class Lion implements Roar {// INSERT CODE HERE
}
```

- A. public void roar() {}
- B. public void roar() throws Exception{}
- C. public void roar() throws Ex1{}
- D. public void roar() throws IllegalArgumentException{}
- E. public void roar() throws Ex2{}

```java title=Example.java
A, C, D, E.
```

## Note

The method is allowed to throw no exceptions at all, making option A correct.

It is also allowed to throw runtime exceptions, making options D and E correct.

Option C is also correct since it matches the signature in the interface.

PreviousNext

## Related

- Java OCA OCP Practice Question 1091
- Java OCA OCP Practice Question 1092
- Java OCA OCP Practice Question 1093
- Java OCA OCP Practice Question 1095
- Java OCA OCP Practice Question 1096
