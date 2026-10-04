---
title: Scala Tutorial - Scala Conditional Operators
nav: Scala Tutorial - Scala Con...
description: Scala conditional operators are listed in the following Table.
section: Imported - java2s Archive
order: 50090
source: https://www.java2s.com/Tutorials/Java/Scala/0200__Scala_Conditional_Operators.html
---
```java title=Example.java
« Previous
```

- Next »

Scala conditional operators are listed in the following Table.

Operator  Operation  Description
&&  and  The values on the left and right of the operator are true. The righthand side is only evaluated if the lefthand side is true.
or  At least one of the values on the left or right is true. The righthand side is only evaluated if the lefthand side is false.
>  greater than  The value on the left is greater than the value on the right.
>=  greater than or equals  The value on the left is greater than or equal to the value on the right.
<  less than  The value on the left is less than the value on the right.
<=  less than or equals The value on the left is less than or equal to the value on the right.
==  equals  The value on the left is the same as the value on the right.
!=  not equals  The value on the left is not the same as the value on the right.

## Note

&& and || are "short-circuiting" operators. They stop evaluating expressions as soon as the answer is known.

In Java, == compares object references only. It doesn't perform a logical equality check, i.e., comparing field values. You use the equals method for that purpose.

Scala uses == for logical equality, but it calls the equals method.

A new method, eq, is available when you want to compare references, but not test for logical equality.

- Next »
- « Previous
