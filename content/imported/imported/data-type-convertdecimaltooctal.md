---
title: Convert Decimal to Octal
nav: Convert Decimal to Octal
description: System.out.printf("Octal value of %d is '%s'.\n", integer, octal);
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertDecimaltoOctal.htm
---
```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    int integer = 1024;

    String octal = Integer.toOctalString(integer);

    System.out.printf("Octal value of %d is '%s'.\n", integer, octal);
    System.out.printf("Octal value of %1$d is '%1$o'.\n", integer);

    int original = Integer.parseInt(octal, 8);
    System.out.printf("Integer value of octal '%s' is %d.", octal, original);
  }
}
```
