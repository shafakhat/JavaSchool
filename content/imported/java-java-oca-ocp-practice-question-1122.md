---
title: Java OCA OCP Practice Question 1122
nav: Java OCA OCP Practice Ques...
description: What is the result of the following when run with java mypkg.Main September 3 2020?
section: Imported - java2s Archive
order: 1099
source: https://web.archive.org/web/20210101014719/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1122.html
---
## Question

What is the result of the following when run with java mypkg.Main September 3 2020?

```java title=Example.java
package mypkg;
publicclass Main {
       publicstaticvoid main(String[] args) {
         for (int i = args.length; i>=0; i--)
            System.out.println(args[i]);
       }
}
```

- A. September
- B. 2020
- C. The code does not compile.
- D. None of the above

```java title=Example.java
D.
```

## Note

There are three arguments passed to the program.

This means that i is 3 on the first iteration of the loop.

The program attempts to print args[3].

Since indexes are zero based in Java, it throws an ArrayIndexOutOfBoundsException.

PreviousNext

## Related

- Java OCA OCP Practice Question 1119
- Java OCA OCP Practice Question 1120
- Java OCA OCP Practice Question 1121
- Java OCA OCP Practice Question 1123
- Java OCA OCP Practice Question 1124
