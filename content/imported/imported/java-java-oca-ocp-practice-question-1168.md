---
title: Java OCA OCP Practice Question 1168
nav: Java OCA OCP Practice Ques...
description: Which line of code, inserted at line p1, causes the application to print 5?
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/20210101014727/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1168.html
---
## Question

Which line of code, inserted at line p1, causes the application to print 5?

```java title=Example.java
package mypkg; //www.java2s.compublicclass Main {
        privateint v = 1;
        protectedboolean outside;

        public Main() {
           // p1
           outside = true;
        }

        public Main(int v) {
           this.v = outside ? v : v+1;
        }

        publicstaticvoid main(String[] bounce) {
           System.out.print(new Main().v);
        }
}
```

- A. this(4);
- B. new Main(4);
- C. this(5);
- D. v = 4;

```java title=Example.java
A.
```

## Note

All of the lines compile but they produce various different results.

The default initialization of a boolean instance variable is false, making outside false at line p1.

this(4) will cause v to be set to 5, while this(5) will cause v to be set to 6.

Since 5 is the number we are looking for, Option A is correct, and Option C is incorrect.

Option B is incorrect.

While the statement does create a new instance of Main, with v having a value of 5, that instance is nested and the value of v does not affect the surrounding instance of Main that the constructor was called in.

Option D is also incorrect.

The value assigned to v is 4, not the target 5.

PreviousNext

## Related

- Java OCA OCP Practice Question 1165
- Java OCA OCP Practice Question 1166
- Java OCA OCP Practice Question 1167
- Java OCA OCP Practice Question 1169
- Java OCA OCP Practice Question 1170
