---
title: Java OCA OCP Practice Question 1176
nav: Java OCA OCP Practice Ques...
description: which method signature could be successfully added to the class as an overloaded version of the m() method?
section: Imported - java2s Archive
order: 1141
source: https://web.archive.org/web/20210101014728/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1176.html
---
## Question

Given the class below,

which method signature could be successfully added to the class as an overloaded version of the m() method?

```java title=Example.java
publicclass Main {
       publicInteger m(int sum) { return sum; }
}
```

- A. public Long m(int sum)
- B. public Long m(int sum, int divisor)
- C. public Integer average(int sum)
- D. private void m(int sum)

```java title=Example.java
B.
```

## Note

Options A and D would not allow the class to compile because two methods in the class cannot have the same name and arguments, but a different return value.

Option C would allow the class to compile, but it is not a valid overloaded form of our m() method since it uses a different method name.

Option B is a valid overloaded version of the m() method, since the name is the same but the argument list differs.

PreviousNext

## Related

- Java OCA OCP Practice Question 1173
- Java OCA OCP Practice Question 1174
- Java OCA OCP Practice Question 1175
- Java OCA OCP Practice Question 1177
- Java OCA OCP Practice Question 1178
