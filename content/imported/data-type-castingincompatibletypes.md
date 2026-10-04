---
title: Casting Incompatible Types
nav: Casting Incompatible Types
description: Imported from the java2s.com archive: Casting Incompatible Types
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/20140622020917/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CastingIncompatibleTypes.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    byte b;
    int i = 257;
    double d = 323.142;
    System.out.println("\nConversion of int to byte.");
    b = (byte) i;
    System.out.println("i and b " + i + " " + b);
    System.out.println("\nConversion of double to int.");
    i = (int) d;
    System.out.println("d and i " + d + " " + i);
    System.out.println("\nConversion of double to byte.");
    b = (byte) d;
    System.out.println("d and b " + d + " " + b);
  }
}
java title=Example.java
Conversion of int to byte.
i and b 257 1
Conversion of double to int.
d and i 323.142 323
Conversion of double to byte.
d and b 323.142 67
```
