---
title: Java Tutorial - Java Boolean Operator
nav: Java Tutorial - Java Boole...
description: The following table lists all Java boolean logical operators.
section: Imported - java2s Archive
order: 50428
source: https://www.java2s.com/Tutorials/Java/Java_Language/3010__Java_Boolean_Operator.html
---
```java title=Example.java
« Previous
```

- Next »

The Boolean logical operators operate on boolean operands.

## Logical Operator List

The following table lists all Java boolean logical operators.

Operator  Result
&  Logical AND
Logical OR
^  Logical XOR (exclusive OR)
Short-circuit OR
&&  Short-circuit AND
!  Logical unary NOT
&=  AND assignment
=  OR assignment
^=  XOR assignment
==  Equal to
!=  Not equal to
? :  Ternary if-then-else

## True table

The following table shows the effect of each logical operation:

A  B  A  B  A & B  A ^ B  !A
False  False  False  False  False  True
True  False  True  False  True  False
False  True  True  False  True  True
True  True  True  True  False  False

The following program demonstrates the boolean logical operators.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    boolean a = true;
    boolean b = false;
    boolean c = a | b;
    boolean d = a & b;
    boolean e = a ^ b;
    boolean f = (!a & b) | (a & !b);
    boolean g = !a;
    System.out.println(" a = " + a);
    System.out.println(" b = " + b);
    System.out.println(" a|b = " + c);
    System.out.println(" a&b = " + d);
    System.out.println(" a^b = " + e);
    System.out.println("!a&b|a&!b = " + f);
    System.out.println(" !a = " + g);
//www.java2s.com
  }
}
]]>
```

The output:

## Example

The following program demonstrates the bitwise logical operators:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int a = 1;//fromwww.java2s.comint b = 2;
    int c = a | b;
    int d = a & b;
    int e = a ^ b;
    int f = (~a & b) | (a & ~b);
    int g = ~a & 0x0f;
    System.out.println(" a = " + a);
    System.out.println(" b = " + b);
    System.out.println(" a|b = " + c);
    System.out.println(" a&b = " + d);
    System.out.println(" a^b = " + e);
    System.out.println("~a&b|a&~b = " + f);
    System.out.println(" ~a = " + g);
  }
}
```

Here is the output from this program:

## Java Logical Operators Shortcut

The OR operator results in true when one operand is true, no matter what the second operand is. The AND operator results in false when one operand is false, no matter what the second operand is. If you use the || and &&, Java will not evaluate the right-hand operand when the outcome can be determined by the left operand alone.

The following code shows how you can use short-circuit logical operator to ensure that a division operation will be valid before evaluating it:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    int denom = 0;
    int num = 3;//www.java2s.comif (denom != 0 && num / denom > 10) {
      System.out.println("Here");
    } else {
      System.out.println("There");
    }
  }
}
```

The output:

If we want to turn of the shortcut behaviour of logical operators we can use & and |.

## Example 2

The following code uses a single & ensures that the increment operation will be applied to e whether c is equal to 1 or not.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    int c = 0;/*www.java2s.com*/int e = 99;
    int d = 0;
    if (c == 1 & e++ < 100)
      d = 100;
    System.out.println("e is " + e);
    System.out.println("d is " + d);
  }
}
```

The output:

- Next »
- « Previous
