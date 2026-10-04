---
title: Java Arithmetic Operator calculate leap year
nav: Java Arithmetic Operator c...
description: if ((year % 400 == 0) || ((year % 4 == 0) && (year % 100 != 0)))
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/20210102113215/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-leap-year.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to check if a year is a leap year.

For example, year 2000 is a leap year

```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    int year = 2004;

    //your code
  }
}
```

```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    int year = 2004;

    if ((year % 400 == 0) || ((year % 4 == 0) && (year % 100 != 0)))
      System.out.println("Year " + year + " is a leap year");
    elseSystem.out.println("Year " + year + " is not a leap year");
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate cylinder volume
- Java Arithmetic Operator calculate distance of two points
- Java Arithmetic Operator calculate floating point value
- Java Arithmetic Operator calculate minutes and seconds
- Java Arithmetic Operator calculate on integer
