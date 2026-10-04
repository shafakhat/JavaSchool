---
title: Reverse an Integer
nav: Reverse an Integer
description: Imported from the java2s.com archive: Reverse an Integer
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20140316035357/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ReverseanInteger.htm
---
```java title=Example.java
class ReverseInt {
  public static void main(String[] args) {
    int num = 1234567890;
    int[] digits = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    int i = 0;
    while (num != 0) {
      digits[i++] = num % 10;
      num /= 10;
    }
    for (i = 0; i < digits.length; i++)
      System.out.print(digits[i]);
  }
}
```
