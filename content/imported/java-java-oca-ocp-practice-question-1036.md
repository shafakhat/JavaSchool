---
title: Java OCA OCP Practice Question 1036
nav: Java OCA OCP Practice Ques...
description: What is the output of the following code? (Choose all that apply)
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1036.html
---
## Question

What is the output of the following code? (Choose all that apply)

```java title=Example.java
1: interface Area {
2:   public default int getArea(int input) { return 2; }
3: }
4: public class Square implements Area {
5:   public String getArea() { return "4"; }
6:   public String getArea(int input) { return "6"; }
7:   public static void main(String[] args) {
8:     System.out.println(new Square().getArea(-1));
9:   }
10: }
```

- A. 2
- B. 4
- C. 6
- D. The code will not compile because of line 5.
- E. The code will not compile because of line 6.
- F. The code will not compile because of line 8.

```java title=Example.java
E.
```

## Note

The code doesn't compile because line 6 contains an incompatible override of the getArea(int input) method defined in the Area interface.

In particular, int and String are not covariant returns types, since int is not a subclass of String.

Note that line 5 compiles without issue; getArea() is an overloaded method that is not related to the parent interface method that takes an int value.

PreviousNext

## Related

- Java OCA OCP Practice Question 1033
- Java OCA OCP Practice Question 1034
- Java OCA OCP Practice Question 1035
- Java OCA OCP Practice Question 1037
- Java OCA OCP Practice Question 1038
