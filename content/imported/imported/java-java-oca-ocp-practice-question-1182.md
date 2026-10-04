---
title: Java OCA OCP Practice Question 1182
nav: Java OCA OCP Practice Ques...
description: What is the best way to call the following method from another class in the same package, assuming the class using the method does not have any static imports?
section: Imported - java2s Archive
order: 1145
source: https://web.archive.org/web/20210101014729/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1182.html
---
## Question

What is the best way to call the following method from another class in the same package, assuming the class using the method does not have any static imports?

```java title=Example.java
package useful;
publicclass Main {
       publicstaticint m(double d) {
          // Implementation omitted
       }
}
```

- A. Main:m(5.92)
- B. Main.m(3.1)
- C. m(4.1)
- D. useful.Main.m(65.3)

```java title=Example.java
B.
```

## Note

Option A is not a valid syntax in Java.

Option C would be correct if there was a static import, but the question specifically says there are not any.

Option D is almost correct, since it is a way to call the method, but the question asks for the best way to call the method.

Option B is the best way to call the method, since we are given that two classes are in the same package, therefore the package name would not be required.

PreviousNext

## Related

- Java OCA OCP Practice Question 1179
- Java OCA OCP Practice Question 1180
- Java OCA OCP Practice Question 1181
- Java OCA OCP Practice Question 1183
- Java OCA OCP Practice Question 1184
