---
title: To convert a byte to it's hexadecimal equivalent
nav: To convert a byte to it's ...
description: Imported from the java2s.com archive: To convert a byte to it's hexadecimal equivalent
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toconvertabytetoitshexadecimalequivalent.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    System.out.println(byteToHex((byte) 123));
  }
  public static String byteToHex(byte b) {
    int i = b & 0xFF;
    return Integer.toHexString(i);
  }
}
//7b
```
