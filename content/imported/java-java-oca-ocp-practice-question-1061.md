---
title: Java OCA OCP Practice Question 1061
nav: Java OCA OCP Practice Ques...
description: A. is correct. calling such methods do not change this object.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20210101014709/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1061.html
---
## Question

In java, Strings are immutable.

A direct implication of this is...

Select 2 options

- A. you cannot call methods like "1234".replace(' 1', '9'); and expect to change the original String.
- B. you cannot change a String object, once it is created.
- C. you can change a String object only by the means of its methods.
- D. you cannot extend String class.
- E. you cannot compare String objects.

```java title=Example.java
Correct Options are: A B
```

## Note

A. is correct. calling such methods do not change this object.

They create a new String object.

You can have a final class whose objects are mutable.

String class implements Comparable interface.

PreviousNext

## Related

- Java OCA OCP Practice Question 1058
- Java OCA OCP Practice Question 1059
- Java OCA OCP Practice Question 1060
- Java OCA OCP Practice Question 1062
- Java OCA OCP Practice Question 1063
