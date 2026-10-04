---
title: Java OCA OCP Practice Question 1009
nav: Java OCA OCP Practice Ques...
description: The case values must evaluate to integer values during compilation.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20210101014701/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1009.html
---
## Question

What is wrong with the following switch statement?

```java title=Example.java
switch(i == 10) {
     case'1':
         ++i;  //www.java2s.combreak;
     case"2":
         --i;
     case 3:
         i *= 5;
         break;
     default
        i %= 3;
}
```

- A. The switch expression must evaluate to an integer value.
- B. The first case specifies a char value.
- C. The second case specifies a String value.
- D. There is a break statement missing in the second case.
- E. An : should follow default.

```java title=Example.java
A, C, and E.
```

## Note

The switch condition must be an integer expression.

The case values must evaluate to integer values during compilation.

A : should follow the default label.

PreviousNext

## Related

- Java OCA OCP Practice Question 1006
- Java OCA OCP Practice Question 1007
- Java OCA OCP Practice Question 1008
- Java OCA OCP Practice Question 1010
- Java OCA OCP Practice Question 1011
