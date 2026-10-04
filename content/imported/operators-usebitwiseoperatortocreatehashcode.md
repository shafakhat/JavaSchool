---
title: Use bitwise operator to create hash code
nav: Use bitwise operator to cr...
description: Imported from the java2s.com archive: Use bitwise operator to create hash code
section: Imported - java2s Archive
order: 1168
source: https://web.archive.org/web/20140312142746/http://www.java2s.com/Tutorial/Java/0060__Operators/Usebitwiseoperatortocreatehashcode.htm
---
```java title=Example.java
public class Main {
  int instanceField;
  {
    int hc = hashCode();
    instanceField = hc;
    for (int i = 0; i < 32; i++) {
      System.out.print((hc & 0x80000000) != 0 ? '1' : '0');
      hc <<= 1;
    }
  }
  public static void main(String[] args) {
    System.out.println(new Main().instanceField);
    System.out.println(new Main().instanceField);
  }
}
```
