---
title: Java Tutorial - Java Arithmetic Operators
nav: Java Tutorial - Java Arith...
description: The operands of the arithmetic operators must be of a numeric type. You cannot use arithmetic operators on boolean types, but you can use them on char types.
section: Imported - java2s Archive
order: 50427
source: https://www.java2s.com/Tutorials/Java/Java_Language/3005__Java_Arithmetic_Operators.html
---
```java title=Example.java
```

Arithmetic operators are used in mathematical expressions.

## All Arithmetic Operators

The following table lists the arithmetic operators:

Operator  Result
---  ---
+  Addition
-  Subtraction (unary minus)
*  Multiplication
/  Division
%  Modulus
++  Increment
+=  Addition assignment
-=  Subtraction assignment
*=  Multiplication assignment
/=  Division assignment
%=  Modulus assignment
--  Decrement

The operands of the arithmetic operators must be of a numeric type. You cannot use arithmetic operators on boolean types, but you can use them on char types.

The basic arithmetic operations are addition, subtraction, multiplication, and division. They behave as you would expect. The minus operator also has a unary form which negates its single operand.

The quick demo below shows how to do a simple calculation in Java with basic arithmetic operators.

```java title=Example.java
publicclass Main {
//fromwww.java2s.compublicstaticvoid main(String args[]) {
    System.out.println("Integer Arithmetic");
    int a = 1 + 1;
    int b = a * 3;
    int c = b / 4;
    int d = c - a;
    int e = -d;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
    System.out.println("e = " + e);
    int x = 42;
    System.out.println("x mod 10 = " + x % 10);
    double y = 42.25;
    System.out.println("y mod 10 = " + y % 10);
  }
}
```

When you run this program, you will see the following output:

The modulus operator, %, returns the remainder of a division operation. The modulus operator can be applied to floating-point types as well as integer types.

## Java Compound Assignment Operators

Statements like the following

```java title=Example.java

a = a + 4;
```

can be rewritten as

```java title=Example.java

a += 4;
```

Both statements perform the same action: they increase the value of a by 4.

Any statement of the form

```java title=Example.java
var = var op expression;
```

can be rewritten as

```java title=Example.java
var op= expression;
```

Here is a sample program that shows several op= operator assignments:

```java title=Example.java
publicclass Main {
/*fromwww.java2s.com*/publicstaticvoid main(String args[]) {
    int a = 1;
    int b = 2;
    int c = 3;
    a += 1;
    b *= 2;
    c += a * b;
    c %= 3;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
  }
}
```

The output of this program is shown here:

## Java Increment and Decrement Operator

++ and -- are Java's increment and decrement operators. The increment operator, ++, increases its operand by one. The decrement operator, --, decreases its operand by one.

Different between Increment and Decrement Operator:

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

The increment and decrement operators are unique in that they can appear both in postfix form and prefix form. In the postfix form they follow the operand, for example, i++. In the prefix form, they precede the operand, for example, --i.

The difference between these two forms appears when the increment and/or decrement operators are part of a larger expression. In the prefix form, the operand is incremented or decremented before the value is used in the expression. In postfix form, the value is used in the expression, and then the operand is modified.

The following table summarizes the difference between Pre-and Post- Increment and Decrement Operations:

| Initial Value of x | Expression | Final Value of y | Final Value of x |
|---|---|---|---|
| 5 | y = x++ | 5 | 6 |
| 5 | y = ++x | 6 | 6 |
| 5 | y = x-- | 5 | 4 |
| 5 | y = --x | 4 | 4 |

For example:

```java title=Example.java

x = 42;
y = ++x;
```

y is set to 43, because the increment occurs before x is assigned to y. Thus, the line

```java title=Example.java

y = ++x;
```

is the equivalent of these two statements:

```java title=Example.java

x = x + 1;
y = x;
```

However, when written like this,

```java title=Example.java

x = 42;
y = x++;
```

the value of x is obtained before the increment operator is executed, so the value of y is 42.

In both cases x is set to 43. The line

```java title=Example.java

y = x++;
```

is the equivalent of these two statements:

```java title=Example.java

y = x;
x = x + 1;
```

The following program demonstrates the increment operator.

```java title=Example.java
publicclass Main {
/*www.java2s.com*/publicstaticvoid main(String args[]) {
    int a = 1;
    int b = 2;
    int c = ++b;
    int d = a++;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
  }
}
```

The output of this program follows:

- « Previous
