---
title: The ? Operator (Ternary)
nav: The ? Operator (Ternary)
description: Imported from the java2s.com archive: The ? Operator (Ternary)
section: Imported - java2s Archive
order: 1139
source: https://web.archive.org/web/20140829091457/http://www.java2s.com/Tutorial/Java/0060__Operators/TheOperatorTernary.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int i, k;
    i = 10;
    k = i < 0 ? -i : i; // get absolute value of i
    System.out.print("Absolute value of ");
    System.out.println(i + " is " + k);
    i = -10;
    k = i < 0 ? -i : i; // get absolute value of i
    System.out.print("Absolute value of ");
    System.out.println(i + " is " + k);
  }
}
java title=Example.java
Absolute value of 10 is 10
Absolute value of -10 is 10
```
