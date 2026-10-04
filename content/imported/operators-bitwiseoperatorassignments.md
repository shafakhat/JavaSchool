---
title: Bitwise Operator Assignments
nav: Bitwise Operator Assignments
description: Imported from the java2s.com archive: Bitwise Operator Assignments
section: Imported - java2s Archive
order: 1155
source: https://web.archive.org/web/20140312135504/http://www.java2s.com/Tutorial/Java/0060__Operators/BitwiseOperatorAssignments.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int a = 1;
    int b = 2;
    int c = 3;
    a |= 4;
    b >>= 1;
    c <<= 1;
    a ^= c;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
  }
}
java title=Example.java
a = 3
b = 1
c = 6
```
