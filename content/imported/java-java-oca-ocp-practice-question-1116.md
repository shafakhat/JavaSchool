---
title: Java OCA OCP Practice Question 1116
nav: Java OCA OCP Practice Ques...
description: Imported from the java2s.com archive: Java OCA OCP Practice Question 1116
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20210101014718/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1116.html
---
## Question

Given the following code, what will be the outcome?

```java title=Example.java
publicclass MyClass extends java.lang.Math {
   publicint add(int x, int y) {
      return x + y;
   } publicint sub(int x, int y) {
      return x - y;
   }
   publicstaticvoid main(String [] a) {
      MyClass f = new MyClass();
      System.out.println("" + f.add(1, 2));
   }
}
```

- A. The code compiles but does not output anything.
- B. "3" is printed out to the console.
- C. The code does not compile.
- D. None of the above.

```java title=Example.java
C.
```

## Note

The code does not compile because it extends the Math class.

Math class has been declared as final.

A class cannot extend a class that has been declared final.

PreviousNext

## Related

- Java OCA OCP Practice Question 1113
- Java OCA OCP Practice Question 1114
- Java OCA OCP Practice Question 1115
- Java OCA OCP Practice Question 1117
- Java OCA OCP Practice Question 1118
