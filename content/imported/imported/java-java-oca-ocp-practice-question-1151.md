---
title: Java OCA OCP Practice Question 1151
nav: Java OCA OCP Practice Ques...
description: Which of the following can fill in the blank to have the code compile successfully?
section: Imported - java2s Archive
order: 1120
source: https://web.archive.org/web/20210101014724/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1151.html
---
## Question

Which of the following can fill in the blank to have the code compile successfully?

```java title=Example.java
package nyc;
publicclass Main {
       publicstaticvoid main(String... args) {
          String[] s = newString[] { "A", "B", "C" };
          String[] times = newString[] { "Day", "Night" };
             for (                     i < 1; i++, j++)
                System.out.println(s[i] + " " + times[j]);
       }
}
```

- A. int i=0; j=0;
- B. int i=0, j=0;
- C. int i=0; int j=0;
- D. int i=0, int j=0;

```java title=Example.java
B.
```

## Note

In a for loop, the type is only allowed to be specified once.

A comma separates multiple variables since they are part of the same statement.

Option B is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1148
- Java OCA OCP Practice Question 1149
- Java OCA OCP Practice Question 1150
- Java OCA OCP Practice Question 1152
- Java OCA OCP Practice Question 1153
