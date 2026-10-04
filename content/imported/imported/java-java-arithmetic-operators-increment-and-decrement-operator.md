---
title: Java Arithmetic Operators Increment and Decrement Operator
nav: Java Arithmetic Operators ...
description: The ++ and the -- are Java's increment and decrement operators.
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20210102113207/http://www.java2s.com/ref/java/java-arithmetic-operators-increment-and-decrement-operator.html
---
## Introduction

The ++ and the -- are Java's increment and decrement operators.

The increment operator increases its operand by one.

The decrement operator decreases its operand by one.

For example, this statement:

```java title=Example.java

x = x + 1;
```

can be rewritten like this by use of the increment operator:

```java title=Example.java

x++;
```

This statement:

```java title=Example.java

x = x - 1;
```

is equivalent to

```java title=Example.java

x--;
```

Java Increment and Decrement Operator can appear in postfix form and prefix form.

In postfix form, they follow the operand.

In prefix form, they precede the operand.

In the prefix form, the operand is incremented or decremented before the value is obtained for use in the expression.

In postfix form, the previous value is obtained for use in the expression, and then the operand is modified.

For example:

```java title=Example.java

x = 42;
y = ++x;
```

In the code above, y is set to 43, because the increment occurs before x is assigned to y.

Thus, the line y=++x; is the equivalent of these two statements:

```java title=Example.java

x = x + 1;
y = x;
```

However, when written like this,

```java title=Example.java

x = 42;
y = x++;
```

The value of x is obtained before the increment operator is executed, so the value of y is 42.

In both cases x is set to 43.

Here, the line y=x++; is the equivalent of these two statements:

```java title=Example.java

y = x;
x = x + 1;
```

The following program demonstrates the increment operator.

```java title=Example.java
// Demonstrate ++ and --.publicclass Main {
  publicstaticvoid main(String args[]) {
    int a = 1;/*www.java2s.com*/int b = 2;
    int c;
    int d;

    c = ++b;
    d = a++;
    c++;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operators Modulus Operator calculate Greatest Common Divisor
- Java Arithmetic Operators Compound Assignment Operators
- Java Arithmetic Operators Compound Assignment Operators Question 1
- Java Bitwise Operators
- Java Bitwise Operators Logical Operators
