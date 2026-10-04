---
title: Java OCA OCP Practice Question 1093
nav: Java OCA OCP Practice Ques...
description: Since count is a class variable that isn't specifically initialized, it defaults to 0.
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20210101014715/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1093.html
---
## Question

What is the output of the following code?

```java title=Example.java
package mypkg; /*www.java2s.com*/publicclass Main {
        privatestaticint count;
        privatestaticString[] stops = newString[] { "Washington",
            "Monroe", "Jackson", "LaSalle" };
        publicstaticvoid main(String[] args) {
           while (count < stops.length) {
              if (stops[count++].length() < 8) {
                 break;
               }
           }
           System.out.println(count);
        }
}
```

- A. 1
- B. 2
- C. 4
- D. The code does not compile.

```java title=Example.java
B.
```

## Note

Since count is a class variable that isn't specifically initialized, it defaults to 0.

On the first iteration of the loop, "Washington", is 11 characters and count is set to 1.

The if statement's body is not run.

The loop then proceeds to the next iteration.

This time, the post-increment operator uses index 1 before setting count to 2.

"Monroe" is checked, which is only 6 characters.

The break statement sends the execution to after the loop and 2 is output.

Option B is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1090
- Java OCA OCP Practice Question 1091
- Java OCA OCP Practice Question 1092
- Java OCA OCP Practice Question 1094
- Java OCA OCP Practice Question 1095
