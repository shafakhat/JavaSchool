---
title: Java Arithmetic Operator remainder operator
nav: Java Arithmetic Operator r...
description: We would like to find out the changes for give numbers of money.
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20210102113219/http://www.java2s.com/ref/java/java-arithmetic-operator-remainder-operator.html
---
## Question

We would like to find out the changes for give numbers of money.

The total money we have is 248 cents.

The code should output the quarters, dimes, nickels, cents it include.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int total = 248;
    //your code here
  }
}
java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int total = 248;
    int quarters = total / 25;
    int whatsLeft = total % 25;
    int dimes = whatsLeft / 10;
    whatsLeft = whatsLeft % 10;
    int nickels = whatsLeft / 5;
    whatsLeft = whatsLeft % 5;
    int cents = whatsLeft;
    System.out.println("From " + total + " cents you get");
    System.out.println(quarters + " quarters");
    System.out.println(dimes + " dimes");
    System.out.println(nickels + " nickels");
    System.out.println(cents + " cents");
  }
}
```

The symbol for the remainder operator is the percent sign (%).

PreviousNext

## Related

- Java Arithmetic Operator Question 9
- Java Arithmetic Operator Question 10
- Java Arithmetic Operator Question 11
- Java Arithmetic Operator separate the Digits in an Integer
- Java Arithmetic Operator solve 2 by 2 linear equations
