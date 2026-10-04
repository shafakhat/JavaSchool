---
title: Java OCA OCP Practice Question 1070
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 1070
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20210101014711/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1070.html
---
## Question

Which of the following statements is/are true?

Select 1 option

- A. Subclasses must define all the abstract methods that the superclass defines.
- B. A class implementing an interface must define all the methods of that interface.
- C. A class cannot override the super class's constructor.
- D. It is possible for two classes to be the superclass of each other.
- E. An interface can implement multiple interfaces.

```java title=Example.java
Correct Option is  : C
```

## Note

A. is wrong. Not if the subclass is also defined abstract!

B. is wrong. Not if the class is defined abstract.

C. is correct. Because constructors are not inherited.

D. and E. are wrong.

Interface cannot "implement" anything.

It can extend multiple interfaces.

The following is a valid declaration:

```java title=Example.java
interface I1 extends I2, I3, I4  {  }
```

PreviousNext

## Related

- Java OCA OCP Practice Question 1067
- Java OCA OCP Practice Question 1068
- Java OCA OCP Practice Question 1069
- Java OCA OCP Practice Question 1071
- Java OCA OCP Practice Question 1072
