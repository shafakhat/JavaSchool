---
title: Convert Decimal to Binary
nav: Convert Decimal to Binary
description: System.out.println("Binary value of " + integer + " is " + binary + ".");
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertDecimaltoBinary.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int integer = 127;
    String binary = Integer.toBinaryString(integer);
    System.out.println("Binary value of " + integer + " is " + binary + ".");

    int original = Integer.parseInt(binary, 2);
    System.out.println("Integer value of binary '" + binary + "' is " + original + ".");
  }

}
```
