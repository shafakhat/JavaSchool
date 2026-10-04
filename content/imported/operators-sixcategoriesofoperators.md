---
title: Six categories of operators
nav: Six categories of operators
description: Unary operators Arithmetic operators Relational and conditional operators Shift and logical operators Assignment operators Other operators
section: Imported - java2s Archive
order: 1297
source: https://web.archive.org/web/20140829094533/http://www.java2s.com/Tutorial/Java/0060__Operators/Sixcategoriesofoperators.htm
---
In Java, there are six categories of operators.
Unary operators Arithmetic operators Relational and conditional operators Shift and logical operators Assignment operators Other operators

```java title=Example.java
Precedence     Operator     Description                          Association
1              ++,--        Postincrement, Postdecrement         R -> L
2              ++,--        Preincrement, Predecrement           R -> L
               +,-          Unary plus, unary minus              R -> L
               ~            Bitwise compliment                   R -> L
               !            Boolean NOT                          R -> L
3              new          Create object                        R -> L
               (type)       Type cast                            R -> L
4              *,/,%        Multiplication, division, remainder  L -> R
5              +,-          Addition, subtraction                L -> R
               +            String concatenation                 L -> R
6              <<, >>, >>>  Left shift, right shift, unsigned right shift     L -> R
7              <, <=, >, >=                                      L -> R
               instanceof   Type comparison                      L -> R
8              ==, !=       Value equality and inequality        L -> R
               ==, !=       Reference equality and inequality    L -> R
9              &            Boolean AND                          L -> R
               &            Bitwise AND                          L -> R
10             ^            Boolean XOR                          L -> R
               ^            Bitwise XOR                          L -> R
11             |            Boolean OR                           L -> R
               |            Bitwise OR                           L -> R
12             &&           Conditional AND                      L -> R
13             ||           Conditional OR                       L -> R
14             ?:           Conditional Ternary Operator         L -> R
15             =,+=,-=,     Assignment Operators                 R -> L
               *=,/ =,%=,
               &=,^=, |=,
               <<=, >> =,
               >>>=
```
