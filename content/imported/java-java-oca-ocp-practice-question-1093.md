---
title: Java OCA OCP Practice Question 1093
nav: Java OCA OCP Practice Ques...
description: package mypkg; /* w w w. ja va 2 s.c o m*/public class Main {
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1093.html
---
## Question

What is the output of the following code?

```java title=Example.java
package mypkg; public class Main {
        private static int count;
        private static String[] stops = new String[] { "Washington",
            "Monroe", "Jackson", "LaSalle" };
        public static void main(String[] args) {
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
