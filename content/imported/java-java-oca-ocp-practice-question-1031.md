---
title: Java OCA OCP Practice Question 1031
nav: Java OCA OCP Practice Ques...
description: 9: publicvoid print() { System.out.println("Square print"); }
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20210101014705/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1031.html
---
## Question

What is the output of the following code?

```java title=Example.java
1: abstractclassPrintable {
2:   publicfinalvoid print() {
         System.out.println("Printable print");
     }
3:     publicstaticvoid main(String[] args) {
4:       Printable p = new Square();
5:       p.print();
6:     }
7: }
8: publicclass Square extendsPrintable {
9:   publicvoid print() { System.out.println("Square print"); }
10:}
```

- A. Printable print
- B. Square print
- C. The code will not compile because of line 4.
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 9.

```java title=Example.java
E.
```

## Note

The code doesn't compile, so options A and B are incorrect.

The issue with line 9 is that print() is marked as final in the superclass Printable, which means it cannot be overridden. There are no errors on any other lines, so options C and D are incorrect.

PreviousNext

## Related

- Java OCA OCP Practice Question 1028
- Java OCA OCP Practice Question 1029
- Java OCA OCP Practice Question 1030
- Java OCA OCP Practice Question 1032
- Java OCA OCP Practice Question 1033
