---
title: Java OCA OCP Practice Question 1163
nav: Java OCA OCP Practice Ques...
description: System.out.print("s1 " + ((s1 == s2) ? "==" : "!=") + " s2");
section: Imported - java2s Archive
order: 1130
source: https://web.archive.org/web/20210101014726/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1163.html
---
## Question

What is the output displayed by the following program?

```java title=Example.java
publicclass Main {
   publicstaticvoid main(String[] args) {
      String s1 = "ab";
      String s2 = "abcd";
      String s3 = "cd";
      String s4 = s1 + s3;/*www.java2s.com*/
      s1 = s4;
      System.out.print("s1 " + ((s1 == s2) ? "==" : "!=") + " s2");
   }

}
```

```java title=Example.java

A.   s1 == s2
B.   s1 != s2
C.   s1
D.   s1 == "abcd"
```

```java title=Example.java
B.
```

## Note

Because s1 and s2 refer to different objects, s1 != s2 is true.

PreviousNext

## Related

- Java OCA OCP Practice Question 1160
- Java OCA OCP Practice Question 1161
- Java OCA OCP Practice Question 1162
- Java OCA OCP Practice Question 1164
- Java OCA OCP Practice Question 1165
