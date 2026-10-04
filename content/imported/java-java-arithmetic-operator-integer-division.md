---
title: Java Arithmetic Operator Integer division
nav: Java Arithmetic Operator I...
description: In Java, if you divide two integers, the result is an integer.
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20210102113218/http://www.java2s.com/ref/java/java-arithmetic-operator-integer-division.html
---
## Question

What is the output of the following program

```java title=Example.java
publicclass Main {
   publicstaticvoid main(String args[]) {
      System.out.println(5 / 4);
      System.out.println(10 / 4);
   }
}
java title=Example.java
1
2
```

## Note

In Java, if you divide two integers, the result is an integer.

The fractional part is truncated.

For example, 5 / 4 is 1 (not 1.25) and 10 / 4 is 2 (not 2.5).

To get an accurate result, make sure that one of the values involved in the division is a number with a decimal point.

For example, 5.0 / 4 is 1.25 and 10 / 4.0 is 2.5.

PreviousNext

## Related

- Java Arithmetic Operator find the number of years
- Java Arithmetic Operator increment and decrement result 1
- Java Arithmetic Operator increment and decrement result 2
- Java Arithmetic Operator Question 1
- Java Arithmetic Operator Question 2
