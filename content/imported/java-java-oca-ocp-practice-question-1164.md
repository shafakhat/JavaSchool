---
title: Java OCA OCP Practice Question 1164
nav: Java OCA OCP Practice Ques...
description: Which of the following can fill in the blank to make the class compile?
section: Imported - java2s Archive
order: 1131
source: https://web.archive.org/web/20210101014726/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1164.html
---
## Question

Which of the following can fill in the blank to make the class compile?

```java title=Example.java
package ai;
publicclass Main {
      compute() { return 10; }
}
```

- A. Public int
- B. Long
- C. void
- D. private String

```java title=Example.java
B.
```

## Note

Option A is incorrect because the public access modifier starts with a lowercase letter.

Options C and D are incorrect because the return types, void and String, are incompatible with the method body that returns an integer value of 10.

Option B is correct and has package-private access.

It uses a return type of Long that the integer value of 10 can be easily assigned to without an explicit cast.

PreviousNext

## Related

- Java OCA OCP Practice Question 1161
- Java OCA OCP Practice Question 1162
- Java OCA OCP Practice Question 1163
- Java OCA OCP Practice Question 1165
- Java OCA OCP Practice Question 1166
