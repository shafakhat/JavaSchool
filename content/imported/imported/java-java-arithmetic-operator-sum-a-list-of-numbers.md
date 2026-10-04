---
title: Java Arithmetic Operator sum a list of numbers
nav: Java Arithmetic Operator s...
description: Imported from the java2s.com archive: Java Arithmetic Operator sum a list of numbers
section: Imported - java2s Archive
order: 1089
source: https://web.archive.org/web/20210102113220/http://www.java2s.com/ref/java/java-arithmetic-operator-sum-a-list-of-numbers.html
---
## Question

We would like to write a program that displays the result of

```java title=Example.java

1 +  2  +  3  +  4  +  5  +  6  +  7  + 8  +  9
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9);
  }
}
```

## Note

We can also use a for loop:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int result = 0;
    for (int i = 1; i <= 9; i++) {
      result += i;//www.java2s.com
    }
    System.out.println(result);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator separate the Digits in an Integer
- Java Arithmetic Operator solve 2 by 2 linear equations
- Java Arithmetic Operator solve quadratic equations
- Java Arithmetic Operator sum the digits in an integer
- Java Boolean Logical Operators truth table
