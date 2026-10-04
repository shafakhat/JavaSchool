---
title: The Bitwise Logical Operators
nav: The Bitwise Logical Operat...
description: Imported from the java2s.com archive: The Bitwise Logical Operators
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/TheBitwiseLogicalOperators.htm
---
```java title=Example.java
A    B    A | B        A & B         A ^ B         ~A
0    0    0            0             0             1
1    0    1            0             1             0
0    1    1            0             1             1
1    1    1            1             0             0
The Bitwise NOT
      00101010   42
     becomes
      11010101
The Bitwise AND
    00101010        42
  & 00001111        15
   __________
    00001010        10
The Bitwise OR
     00101010        42
   | 00001111        15
    _________
     00101111        47
The Bitwise XOR
   00101010        42
 ^ 00001111        15
   _________
   00100101        37
```
