---
title: Convert base64 string to a byte array
nav: Convert base64 string to a...
description: Imported from the java2s.com archive: Convert base64 string to a byte array
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20101009080046/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Convertbase64stringtoabytearray.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] buf = new byte[] { 0x12, 0x23 };
    String s = new sun.misc.BASE64Encoder().encode(buf);
    buf = new sun.misc.BASE64Decoder().decodeBuffer(s);
  }
}
```
