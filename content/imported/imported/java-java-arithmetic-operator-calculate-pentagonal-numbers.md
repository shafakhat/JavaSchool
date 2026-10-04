---
title: Java Arithmetic Operator calculate pentagonal numbers
nav: Java Arithmetic Operator c...
description: A pentagonal number is defined as n(3n-1)/2 for n = 1, 2, . . ., and so on.
section: Imported - java2s Archive
order: 1063
source: https://web.archive.org/web/20210102113215/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-pentagonal-numbers.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

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
