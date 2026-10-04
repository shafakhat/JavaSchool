---
title: Java OCA OCP Practice Question 1158
nav: Java OCA OCP Practice Ques...
description: publicvoid nested() { nested(2,true); } // g1 publicint nested(int level, boolean height) { return nested(level); }
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/20210101014725/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1158.html
---
## Question

What is true about the following program?

```java title=Example.java
package mypkg; publicclass Main {
        publicvoid nested() { nested(2,true); } // g1 publicint nested(int level, boolean height) { return nested(level); }
        publicint nested(int level) { return level+1; }; // g2
     ?
        publicstaticvoid main(String[] v) {
           System.out.print(new Main().nested());
        }
}
```

- A. It compiles successfully and prints 3 at runtime.
- B. It does not compile because of line g1.
- C. It does not compile because of line g2.
- D. It does not compile for some other reason.

```java title=Example.java
D.
```

## Note

The three overloaded versions of nested() compile without issue, since each method takes a different set of input arguments, making Options B and C incorrect.

The code does not compile, though, due to the first line of the main() method, making Option A incorrect.

The no-argument version of the nested() method does not return a value, and trying to output a void return type in the print() method throws an exception at runtime.

PreviousNext

## Related

- Java OCA OCP Practice Question 1155
- Java OCA OCP Practice Question 1156
- Java OCA OCP Practice Question 1157
- Java OCA OCP Practice Question 1159
- Java OCA OCP Practice Question 1160
