---
title: Java Arithmetic Operator calculate/approximate PI
nav: Java Arithmetic Operator c...
description: }//www.java2s.comprivatestaticdouble approximatePi(int index) {
section: Imported - java2s Archive
order: 1065
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-calculateapproximate-pi.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

Pi can be computed using the following formula:

```java title=Example.java

pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)
```

We would like to write a program that displays the result of

```java title=Example.java

4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11)
```

and

```java title=Example.java

4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13)
```

```java title=Example.java
publicclass Main{
  publicstaticvoid main(String[] args) {
    System.out.println(4 * (1.0 - (1 / 3) + (1 / 5) -
              (1 / 7) + (1 / 9) - (1 / 11)));
    System.out.println(4 * (1.0 - (1 / 3) + (1 / 5) - (1 / 7)
               + (1 / 9) - (1 / 11) + (1 / 13)));
  }
}
```

## Note

We can also use loop:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println(approximatePi(11));
    System.out.println(approximatePi(13));
  }//www.java2s.comprivatestaticdouble approximatePi(int index) {
    boolean positive = true;
    double sum = 0.0;
    for (int i = 1; i <= index; i += 2) {
      if (positive) {
        sum += (1.0 / i);
        positive = false;
      } else {
        sum -= (1.0 / i);
        positive = true;
      }
    }

    return 4.0 * sum;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate on integer
- Java Arithmetic Operator calculate pentagonal numbers
- Java Arithmetic Operator calculate tips
- Java Arithmetic Operator compound operator result
- Java Arithmetic Operator compute expressions
