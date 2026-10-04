---
title: Java OCA OCP Practice Question 1101
nav: Java OCA OCP Practice Ques...
description: This is a correct loop to go through an ArrayList or List starting from the beginning.
section: Imported - java2s Archive
order: 1082
source: https://web.archive.org/web/20210101014716/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1101.html
---
## Question

What is the output of the following?

```java title=Example.java
import java.util.Arrays;
import java.util.List;

publicclass Main {
   publicstaticvoid main(String[] args) {
      List<String> v = Arrays.asList("can", "cup");
      for (int c = 0; c < v.size(); c++)
         System.out.print(v.get(c) + ",");

   }//fromwww.java2s.com
}
```

- A. can,cup,
- B. cup,can,
- C. The code does not compile.
- D. None of the above

```java title=Example.java
A.
```

## Note

This is a correct loop to go through an ArrayList or List starting from the beginning.

It starts with index 0 and goes to the last index in the list.

Option A is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1098
- Java OCA OCP Practice Question 1099
- Java OCA OCP Practice Question 1100
- Java OCA OCP Practice Question 1102
- Java OCA OCP Practice Question 1103
