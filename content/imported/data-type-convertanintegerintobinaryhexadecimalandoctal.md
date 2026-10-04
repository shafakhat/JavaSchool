---
title: Convert an integer into binary, hexadecimal, and octal.
nav: Convert an integer into bi...
description: System.out.println(num + " in binary: " + Integer.toBinaryString(num));
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertanintegerintobinaryhexadecimalandoctal.htm
---
```java title=Example.java
class StringConversions {
  publicstaticvoid main(String args[]) {
    int num = 19648;
    System.out.println(num + " in binary: " + Integer.toBinaryString(num));
    System.out.println(num + " in octal: " + Integer.toOctalString(num));
    System.out.println(num + " in hexadecimal: " + Integer.toHexString(num));
  }
}
```
