---
title: Java OCA OCP Practice Question 1033
nav: Java OCA OCP Practice Ques...
description: 9: publicvoid dive(int depth) { System.out.println("MySubClass diving"); }
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1033.html
---
## Question

What is the output of the following code?

```java title=Example.java

1: publicabstractclass MyClass {
2:   publicabstractvoid dive() {};
3:   publicstaticvoid main(String[] args) {
4:     MyClass m = new MySubClass();
5:     m.dive(); //www.java2s.com
6:   }
7: }
8: class MySubClass extends MyClass {
9:   publicvoid dive(int depth) { System.out.println("MySubClass diving"); }
10: }
```

- A. MySubClass diving
- B. The code will not compile because of line 2.
- C. The code will not compile because of line 8.
- D. The code will not compile because of line 9.
- E. The output cannot be determined from the code provided.

```java title=Example.java
B.
```

## Note

This may look like a complex question, but it is actually quite easy.

Line 2 contains an invalid definition of an abstract method.

Abstract methods cannot contain a body, so the code will not compile and option B is the correct answer.

If the body {} was removed from line 2, the code would still not compile, although it would be line 8 that would throw the compilation error.

Since dive() in MyClass is abstract and MySubClass extends MyClass, then it must implement an overridden version of dive().

The method on line 9 is an overloaded version of dive(), not an overridden version, so MySubClass is an invalid subclass and will not compile.

PreviousNext

## Related

- Java OCA OCP Practice Question 1030
- Java OCA OCP Practice Question 1031
- Java OCA OCP Practice Question 1032
- Java OCA OCP Practice Question 1034
- Java OCA OCP Practice Question 1035
