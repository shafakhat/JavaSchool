---
title: Java OCA OCP Practice Question 1006
nav: Java OCA OCP Practice Ques...
description: Which of the following statements can be inserted in the blank line so that the code will compile successfully? (Choose all that apply)
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1006.html
---
## Question

Which of the following statements can be inserted in the blank line so that the code will compile successfully? (Choose all that apply)

```java title=Example.java
publicinterfacePrintable {}
publicclassShapeimplementsPrintable {
   publicstaticvoid main(String[] args) {
          frog = new Square();
   }
}
publicclassRectangleextendsShape {}
publicclass Square extendsShape {}
```

- A. Shape
- B. Square
- C. Rectangle
- D. Printable
- E. Object
- F. Long

```java title=Example.java
A, B, D, E.
```

## Note

The blank can be filled with any class or interface that is a super type of Square.

Option A is a superclass of Square, and option B is the same class, so both are correct.

Rectangle is not a superclass of Square, so option C is incorrect.

Square inherits the Printable interface, so option D is correct.

All classes inherit Object, so option E is correct.

Finally, Long is an unrelated class that is not a superclass of Square, and is therefore incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1003
- Java OCA OCP Practice Question 1004
- Java OCA OCP Practice Question 1005
- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1008
