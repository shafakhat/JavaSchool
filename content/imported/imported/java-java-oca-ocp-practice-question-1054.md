---
title: Java OCA OCP Practice Question 1054
nav: Java OCA OCP Practice Ques...
description: Only methods that are inherited can be overridden and private methods are not inherited.
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20210101014708/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1054.html
---
## Question

Which of the following statements are true?

Select 2 options

- A. Private methods cannot be overridden in subclasses.
- B. A subclass can override any method in a non-final superclass.
- C. An overriding method can declare that it throws a wider spectrum of checked exceptions than the method it is overriding.
- D. The parameter list of an overriding method must be a subset of the parameter list of the method that it is overriding.
- E. The overriding method may opt not to declare any throws clause even if the original method has a throws clause.

```java title=Example.java
Correct Options are  : A E
```

## Note

A. is a correct answer.

Only methods that are inherited can be overridden and private methods are not inherited.

B. is wrong.

Only the methods that are not declared to be final can be overridden.

private methods are not inherited so they cannot be overridden either.

C. and D. are wrong.

An overriding method must have the same parameters.

E. is a correct answer.

Empty set of exceptions is a valid subset of the set of exceptions thrown by the original method so an overriding method can choose to not have any throws clause.

A method can be overridden by defining a method with the same signature(name and parameter list) and return type as the method in a superclass.

The return type can be a subclass of the original method's return type.

Only methods that are accessible can be overridden.

A final method cannot be overridden.

An overriding method cannot exhibit behavior that contradicts the declaration of the original method.

A subclass may have a static method with the same signature as a static method in the base class but it is not called overriding.

PreviousNext

## Related

- Java OCA OCP Practice Question 1051
- Java OCA OCP Practice Question 1052
- Java OCA OCP Practice Question 1053
- Java OCA OCP Practice Question 1055
- Java OCA OCP Practice Question 1056
