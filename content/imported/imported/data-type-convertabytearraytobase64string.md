---
title: Convert a byte array to base64 string
nav: Convert a byte array to ba...
description: Imported from the java2s.com archive: Convert a byte array to base64 string
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertabytearraytobase64string.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {

    byte[] buf = newbyte[] { 0x12, 0x23 };
    String s = new sun.misc.BASE64Encoder().encode(buf);
  }
}
```
