---
title: Java Arithmetic Operator calculate pentagonal numbers
nav: Java Arithmetic Operator c...
description: A pentagonal number is defined as n(3n-1)/2 for n = 1, 2, . . ., and so on.
section: Imported - java2s Archive
order: 1063
source: https://web.archive.org/web/20210102113215/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-pentagonal-numbers.html
---
## Question

A pentagonal number is defined as n(3n-1)/2 for n = 1, 2, . . ., and so on.

The first few numbers are 1, 5, 12, 22, . . . .

We would like to write a method with the following header that returns a pentagonal number:

```java title=Example.java
publicstaticint getPentagonalNumber(int n)
```

```java title=Example.java
publicclass Main {

    publicstaticvoid main(String[] args) {

        for (int i = 1; i <= 100; i++) {

            System.out.printf("%10s",(i % 8 != 0) ? getPentagonalNumber(i) + " " : getPentagonalNumber(i) + "\n");

        }//www.java2s.com
    }

    publicstaticint getPentagonalNumber(int n) {
       //your code here
    }
}
```

```java title=Example.java
publicclass Main {

    publicstaticvoid main(String[] args) {

        for (int i = 1; i <= 100; i++) {

            System.out.printf("%10s",(i % 8 != 0) ? getPentagonalNumber(i) + " " : getPentagonalNumber(i) + "\n");

        }
    }

    publicstaticint getPentagonalNumber(int n) {
        return n * (3 * n - 1) / 2;
    }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate leap year
- Java Arithmetic Operator calculate minutes and seconds
- Java Arithmetic Operator calculate on integer
- Java Arithmetic Operator calculate tips
- Java Arithmetic Operator calculate/approximate PI
