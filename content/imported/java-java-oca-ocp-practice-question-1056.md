---
title: Java OCA OCP Practice Question 1056
nav: Java OCA OCP Practice Ques...
description: What will happen if you add the statement System.out.println(5 / 0); to a working main() method?
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20210101014708/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1056.html
---
## Question

What will happen if you add the statement System.out.println(5 / 0); to a working main() method?

- A. It will not compile.
- B. It will not run.
- C. It will run and throw an ArithmeticException.
- D. It will run and throw an IllegalArgumentException.
- E. None of the above.

```java title=Example.java
C.
```

## Note

The compiler tests the operation for a valid type but not a valid result, so the code will still compile and run.

At runtime, evaluation of the parameter takes place before passing it to the print() method, so an ArithmeticException object is raised.

PreviousNext

## Related

- Java OCA OCP Practice Question 1053
- Java OCA OCP Practice Question 1054
- Java OCA OCP Practice Question 1055
- Java OCA OCP Practice Question 1057
- Java OCA OCP Practice Question 1058
