---
title: Convert base64 string to a byte array
nav: Convert base64 string to a...
description: Imported from the java2s.com archive: Convert base64 string to a byte array
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertbase64stringtoabytearray.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {

    byte[] buf = newbyte[] { 0x12, 0x23 };
    String s = new sun.misc.BASE64Encoder().encode(buf);

    buf = new sun.misc.BASE64Decoder().decodeBuffer(s);
  }
}
```
