---
title: Demonstrate the boolean logical operators
nav: Demonstrate the boolean lo...
description: Imported from the java2s.com archive: Demonstrate the boolean logical operators
section: Imported - java2s Archive
order: 1129
source: https://web.archive.org/web/20140829090256/http://www.java2s.com/Tutorial/Java/0060__Operators/Demonstratethebooleanlogicaloperators.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    boolean a = true;
    boolean b = false;
    boolean c = a | b;
    boolean d = a & b;
    boolean e = a ^ b;
    boolean f = (!a & b) | (a & !b);
    boolean g = !a;
    System.out.println("        a = " + a);
    System.out.println("        b = " + b);
    System.out.println("      a|b = " + c);
    System.out.println("      a&b = " + d);
    System.out.println("      a^b = " + e);
    System.out.println("!a&b|a&!b = " + f);
    System.out.println("       !a = " + g);
  }
}
java title=Example.java
a = true
b = false
a|b = true
a&b = false
a^b = true
!a&b|a&!b = true
!a = false
```
