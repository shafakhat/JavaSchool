---
title: Java OCA OCP Practice Question 103
nav: Java OCA OCP Practice Ques...
description: v2 is a generic collection, so the compiler checks the types of arguments to add().
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20210101014437/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-103.html
---
## Question

Give the following declarations:

```java title=Example.java
Vector v1;
Vector<String> v2;
```

What are the advantages of using v2 rather than v1?

- A. add anything other than a string to v2 results in a compiler error.
- B. add anything other than a string to v2 causes a runtime exception to be thrown.
- C. add anything other than a string to v2 causes a checked exception to be thrown.
- D. add a string to v2 takes less time than adding one to v1.
- E. The methods of v2 are synchronized.

```java title=Example.java
A.
```

## Note

v2 is a generic collection, so the compiler checks the types of arguments to add().

PreviousNext

## Related

- Java OCA OCP Practice Question 100
- Java OCA OCP Practice Question 101
- Java OCA OCP Practice Question 102
- Java OCA OCP Practice Question 104
- Java OCA OCP Practice Question 105
