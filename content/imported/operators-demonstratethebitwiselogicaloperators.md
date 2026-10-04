---
title: Demonstrate the bitwise logical operators
nav: Demonstrate the bitwise lo...
description: "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
section: Imported - java2s Archive
order: 1153
source: https://web.archive.org/web/20140312141014/http://www.java2s.com/Tutorial/Java/0060__Operators/Demonstratethebitwiselogicaloperators.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    String binary[] = {
      "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111",
      "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"
    };
    int a = 3; // 0 + 2 + 1 or 0011 in binary
    int b = 6; // 4 + 2 + 0 or 0110 in binary
    int c = a | b;
    int d = a & b;
    int e = a ^ b;
    int f = (~a & b) | (a & ~b);
    int g = ~a & 0x0f;
    System.out.println("        a = " + binary[a]);
    System.out.println("        b = " + binary[b]);
    System.out.println("      a|b = " + binary[c]);
    System.out.println("      a&b = " + binary[d]);
    System.out.println("      a^b = " + binary[e]);
    System.out.println("~a&b|a&~b = " + binary[f]);
    System.out.println("       ~a = " + binary[g]);
  }
}
java title=Example.java
a = 0011
b = 0110
a|b = 0111
a&b = 0010
a^b = 0101
~a&b|a&~b = 0101
~a = 1100
```
