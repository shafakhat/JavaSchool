---
title: Java OCA OCP Practice Question 1029
nav: Java OCA OCP Practice Ques...
description: Concrete classes are, by definition, not abstract, so option A is incorrect.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20210101014704/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1029.html
---
## Question

Which of the following is true about a concrete subclass?

Choose all that apply

- A. A concrete subclass can be declared as abstract.
- B. A concrete subclass must implement all inherited abstract methods.
- C. A concrete subclass must implement all methods defined in an inherited interface.
- D. A concrete subclass cannot be marked as final.
- E. Abstract methods cannot be overridden by a concrete subclass.

```java title=Example.java
B.
```

## Note

Concrete classes are, by definition, not abstract, so option A is incorrect.

A concrete class must implement all inherited abstract methods, so option B is correct.

Option C is incorrect; a superclass may have already implemented an inherited interface, so the concrete subclass would not need to implement the method.

Concrete classes can be both final and not final, so option D is incorrect.

Finally, abstract methods must be overridden by a concrete subclass, so option E is incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1026
- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1030
- Java OCA OCP Practice Question 1031
