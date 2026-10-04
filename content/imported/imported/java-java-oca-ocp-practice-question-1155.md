---
title: Java OCA OCP Practice Question 1155
nav: Java OCA OCP Practice Ques...
description: Which statement (exactly one) is true about the following program?
section: Imported - java2s Archive
order: 1123
source: https://web.archive.org/web/20210101014725/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1155.html
---
## Question

Which statement (exactly one) is true about the following program?

```java title=Example.java
publicclass Main {
   publicstaticvoid main(String[] args) {
      double d1 = 1.0;
      double d2 = 0.0;
      byte b = 1;
      d1 = d1 / d2;//fromwww.java2s.com
      b = (byte) d1;
      System.out.print(b);
   }
}
```

- A. It results in the throwing of an ArithmeticException.
- B. It results in the throwing of a DivideByZeroException .
- C. It displays the value 1.5.
- D. It displays the value -1.

```java title=Example.java
D.
```

## Note

Floating-point operations do not throw exceptions.

This eliminates answers A and B.

It would be impossible for a byte value to be displayed as 1.5.

The only answer left is D.

PreviousNext

## Related

- Java OCA OCP Practice Question 1152
- Java OCA OCP Practice Question 1153
- Java OCA OCP Practice Question 1154
- Java OCA OCP Practice Question 1156
- Java OCA OCP Practice Question 1157
