---
title: Java OCA OCP Practice Question 1080
nav: Java OCA OCP Practice Ques...
description: Which of the following statements are true? (Choose all that apply)
section: Imported - java2s Archive
order: 1061
source: https://web.archive.org/web/20210101014713/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1080.html
---
## Question

Which of the following statements are true? (Choose all that apply)

- A. You can declare a method with Exception as the return type.
- B. You can declare any subclass of Error in the throws part of a method declaration.
- C. You can declare any subclass of Exception in the throws part of a method declaration.
- D. You can declare any subclass of Object in the throws part of a method declaration.
- E. You can declare any subclass of RuntimeException in the throws part of a method declaration.

```java title=Example.java
A, B, C, E.
```

## Note

Classes listed in the throws part of a method declaration must extend java.lang.Throwable.

This includes Error, Exception, and RuntimeException.

Arbitrary classes such as String can't go there.

Any Java type, including Exception, can be declared as the return type.

This will simply return the object rather than throw an exception.

PreviousNext

## Related

- Java OCA OCP Practice Question 1077
- Java OCA OCP Practice Question 1078
- Java OCA OCP Practice Question 1079
- Java OCA OCP Practice Question 1081
- Java OCA OCP Practice Question 1082
