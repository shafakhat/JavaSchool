---
title: Java OCA OCP Practice Question 108
nav: Java OCA OCP Practice Ques...
description: B, C, D, E, and F are incorrect; these lines all use correct syntax.
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/20210101014438/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-108.html
---
## Question

Given:

```java title=Example.java

1. enum Pet { //www.java2s.com
2.   DOG("woof"), CAT("meow"), FISH("burble");
3.   String sound;
4.   Pet(String s) { sound = s; }
5. }
6. class TestEnum {
7.   static Pet a;
8.   publicstaticvoid main(String[] args) {
9.     System.out.println(a.DOG.sound + " " + a.FISH.sound);
10.   }
11. }
```

What is the result?

- A. woof burble
- B. Multiple compilation errors
- C. Compilation fails due to an error on line 2
- D. Compilation fails due to an error on line 3
- E. Compilation fails due to an error on line 4
- F. Compilation fails due to an error on line 9

```java title=Example.java
A is correct; enums can have constructors and variables.
```

## Note

B, C, D, E, and F are incorrect; these lines all use correct syntax.

PreviousNext

## Related

- Java OCA OCP Practice Question 105
- Java OCA OCP Practice Question 106
- Java OCA OCP Practice Question 107
- Java OCA OCP Practice Question 109
- Java OCA OCP Practice Question 110
