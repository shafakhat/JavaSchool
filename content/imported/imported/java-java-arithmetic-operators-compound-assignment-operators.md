---
title: Java Arithmetic Operators Compound Assignment Operators
nav: Java Arithmetic Operators ...
description: Java Arithmetic Compound Assignment Operators can combine an arithmetic operation with an assignment.
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20210102113207/http://www.java2s.com/ref/java/java-arithmetic-operators-compound-assignment-operators.html
---
## Introduction

Java Arithmetic Compound Assignment Operators can combine an arithmetic operation with an assignment.

For the following statement:

```java title=Example.java

a = a + 4;
```

In Java, you can rewrite this statement as shown here:

```java title=Example.java

a += 4;
```

This version uses the += compound assignment operator.

Both statements perform the same action: they increase the value of a by 4.

Here is another example,

```java title=Example.java

a = a % 2;
```

which can be expressed as

```java title=Example.java

a %= 2;
```

In this case, the %= obtains the remainder of a /2 and puts that result back into a.

There are compound assignment operators for all of the arithmetic, binary operators.

Any statement of the form

```java title=Example.java
var = var op expression;
```

can be rewritten as

```java title=Example.java
var op= expression;
```

The following code shows several op= assignments:

```java title=Example.java
// Demonstrate several assignment operators.publicclass Main {
  publicstaticvoid main(String args[]) {
    int a = 1;//fromwww.java2s.comint b = 2;
    int c = 3;

    a += 5;
    b *= 4;
    c += a * b;
    c %= 6;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operators Modulus Operator start new line every 10 elements
- Java Arithmetic Operators Modulus Operator find three digit palindrome number
- Java Arithmetic Operators Modulus Operator calculate Greatest Common Divisor
- Java Arithmetic Operators Compound Assignment Operators Question 1
- Java Arithmetic Operators Increment and Decrement Operator
