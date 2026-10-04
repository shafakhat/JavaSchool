---
title: Java OCA OCP Practice Question 1128
nav: Java OCA OCP Practice Ques...
description: The continue statement is useless here since there is no code later in the loop to skip.
section: Imported - java2s Archive
order: 1104
source: https://web.archive.org/web/20210101014720/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1128.html
---
## Question

What is the output of the following code?

```java title=Example.java
package mypkg; //www.java2s.compublicclass Main {
        privatestaticint count;
        privatestaticString[] stops = newString[] { "Washington",
            "Monroe", "Jackson", "LaSalle" };
        publicstaticvoid main(String[] args) {
           while (count < stops.length) {
              if (stops[count++].length() < 8) {
                 continue;
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
C.
```

## Note

The continue statement is useless here since there is no code later in the loop to skip.

The continue statement merely resumes execution at the next iteration of the loop, which is what would happen if the if-then statement was empty.

Therefore, count increments for each element of the array.

The code outputs 4, and Option C is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1125
- Java OCA OCP Practice Question 1126
- Java OCA OCP Practice Question 1127
- Java OCA OCP Practice Question 1129
- Java OCA OCP Practice Question 1130
