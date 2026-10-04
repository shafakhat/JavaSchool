---
title: Java OCA OCP Practice Question 1010
nav: Java OCA OCP Practice Ques...
description: Which of the following may only be hidden and not overridden?
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1010.html
---
## Question

Which of the following may only be hidden and not overridden?

Choose all that apply

- A. private instance methods
- B. protected instance methods
- C. public instance methods
- D. static methods
- E. public variables
- F. private variables

```java title=Example.java
A, D, E, F.
```

## Note

First off, options B and C are incorrect because protected and public methods may be overridden, not hidden.

Option A is correct because private methods are always hidden in a subclass.

Option D is also correct because static methods cannot be overridden, only hidden.

Options E and F are correct because variables may only be hidden, regardless of the access modifier.

PreviousNext

## Related

- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1008
- Java OCA OCP Practice Question 1009
- Java OCA OCP Practice Question 1011
- Java OCA OCP Practice Question 1012
