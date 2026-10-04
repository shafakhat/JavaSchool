---
title: Java OCA OCP Practice Question 1034
nav: Java OCA OCP Practice Ques...
description: The code compiles and runs without issues, so Options C and D are incorrect.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1034.html
---
## Question

What is the output of the following application?

```java title=Example.java
package mypkg; publicclass Main {
  publicstaticvoid main(String[] dribble) {
     try {
        System.out.print(1);
        thrownewClassCastException();
     } catch (ArrayIndexOutOfBoundsException ex) {
        System.out.print(2);
     } catch (Throwable ex) {
        System.out.print(3);
     } finally {
        System.out.print(4);
     }
     System.out.print(5);
  }
}
```

- A. 1345
- B. 1235
- C. The code does not compile.
- D. The code compiles but throws an exception at runtime.

```java title=Example.java
A.
```

## Note

The code compiles and runs without issues, so Options C and D are incorrect.

The try block throws a ClassCastException.

Since ClassCastException is not a subclass of ArrayIndexOutOfBoundsException, the first catch block is skipped.

For the second catch block, ClassCastException is a subclass of Throwable, so that block is executed.

Then, the finally block is executed and then control returns to the main() method with no exception being thrown.

The result is that 1345 is printed, making Option A the correct answer.

PreviousNext

## Related

- Java OCA OCP Practice Question 1031
- Java OCA OCP Practice Question 1032
- Java OCA OCP Practice Question 1033
- Java OCA OCP Practice Question 1035
- Java OCA OCP Practice Question 1036
