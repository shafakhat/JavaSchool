---
title: Java OCA OCP Practice Question 102
nav: Java OCA OCP Practice Ques...
description: What is the result of compiling and executing the following class?
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20210101014437/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-102.html
---
## Question

What is the result of compiling and executing the following class?

```java title=Example.java
package sports; //fromwww.java2s.compublicclass MyClass {
        String color = "red";
        privatevoid printColor(String color) {
           color = "purple";
           System.out.print(color);
        }
        publicstaticvoid main(String[] rider) {
           new MyClass().printColor("blue");
        }
}
```

- A. red
- B. purple
- C. blue
- D. It does not compile.

```java title=Example.java
B.
```

## Note

First off, the color variable defined in the instance and set to red is ignored in the method printColor() as local scope overrides instance scope, so Option A is incorrect.

The value of color passed to the printColor() method is blue, but that is lost by the assignment to purple, making Option B the correct answer and Option C incorrect.

Option D is incorrect as the code compiles and runs without issue.

PreviousNext

## Related

- Java OCA OCP Practice Question 99
- Java OCA OCP Practice Question 100
- Java OCA OCP Practice Question 101
- Java OCA OCP Practice Question 103
- Java OCA OCP Practice Question 104
