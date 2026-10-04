---
title: Java OCA OCP Practice Question 1087
nav: Java OCA OCP Practice Ques...
description: The first time through the loop, the index is 0 and A, is output.
section: Imported - java2s Archive
order: 1068
source: https://web.archive.org/web/20210101014714/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1087.html
---
## Question

What does the following code output?

```java title=Example.java
publicstaticvoid main(String[] args) {
        List<String> c = Arrays.asList("A", "B");
        for (int type = 0; type < c.size();) {
          System.out.print(c.get(type) + ",");
          break;
        }
        System.out.print("end");
}
```

- A. A,end
- B. A,B,end
- C. The code does not compile.
- D. None of the above

```java title=Example.java
A.
```

## Note

The first time through the loop, the index is 0 and A, is output.

The break statement then skips all remaining executions on the loop and the main() method ends.

If there was no break keyword, this would be an infinite loop.

PreviousNext

## Related

- Java OCA OCP Practice Question 1084
- Java OCA OCP Practice Question 1085
- Java OCA OCP Practice Question 1086
- Java OCA OCP Practice Question 1088
- Java OCA OCP Practice Question 1089
