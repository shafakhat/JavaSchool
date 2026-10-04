---
title: Java OCA OCP Practice Question 1140
nav: Java OCA OCP Practice Ques...
description: The inner loop executes twice for each of those iterations of the outer loop.
section: Imported - java2s Archive
order: 1112
source: https://web.archive.org/web/20210101014722/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1140.html
---
## Question

How many lines does the following code output?

```java title=Example.java
import java.util.*;
publicclass Main {
        publicstaticvoid main(String[] args) {
           List<String> v = Arrays.asList("OCA", "OCP");
           for (String e1 : v)
              for (String e2 : v)
                 System.out.println(e1 + " " + e2);
        }
}
```

- A. One
- B. Four
- C. The code does not compile.
- D. The code compiles but throws an exception at runtime.

```java title=Example.java
B.
```

## Note

Looping through the same list multiple times is allowed.

The outer loop executes twice.

The inner loop executes twice for each of those iterations of the outer loop.

Therefore, the inner loop executes four times, and Option B is correct.

PreviousNext

## Related

- Java OCA OCP Practice Question 1137
- Java OCA OCP Practice Question 1138
- Java OCA OCP Practice Question 1139
- Java OCA OCP Practice Question 1141
- Java OCA OCP Practice Question 1142
