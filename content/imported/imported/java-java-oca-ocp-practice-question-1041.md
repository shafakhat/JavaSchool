---
title: Java OCA OCP Practice Question 1041
nav: Java OCA OCP Practice Ques...
description: 2: privatevoid fly() { System.out.println("Shape is flying"); }
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20210101014706/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1041.html
---
## Question

What is the result of the following code?

```java title=Example.java

1: publicabstractclassShape {
2:   privatevoid fly() { System.out.println("Shape is flying"); }
3:   publicstaticvoid main(String[] args) {
4:     Shape bird = newRectangle();
5:     bird.fly(); /*www.java2s.com*/
6:   }
7: }
8: classRectangleextendsShape {
9:   protectedvoid fly() { System.out.println("Rectangle is flying"); }
10: }
```

- A. Shape is flying
- B. Rectangle is flying
- C. The code will not compile because of line 4.
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 9.

```java title=Example.java
A.
```

## Note

The code compiles and runs without issue, so options C, D, and E are incorrect.

The trick here is that the method fly() is marked as private in the parent class Shape, which means it may only be hidden, not overridden.

With hidden methods, the specific method used depends on where it is referenced.

Since it is referenced within the Shape class, the method declared on line 2 was used, and option A is correct.

Alternatively, if the method was referenced within the Rectangle class, or if the method in the parent class was marked as protected and overridden in the subclass, then the method on line 9 would have been used.

PreviousNext

## Related

- Java OCA OCP Practice Question 1038
- Java OCA OCP Practice Question 1039
- Java OCA OCP Practice Question 1040
- Java OCA OCP Practice Question 1042
- Java OCA OCP Practice Question 1043
