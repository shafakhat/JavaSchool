---
title: Convert an UNSIGNED byte to a JAVA type
nav: Convert an UNSIGNED byte t...
description: Imported from the java2s.com archive: Convert an UNSIGNED byte to a JAVA type
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertanUNSIGNEDbytetoaJAVAtype.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    byte b1 = 127;
    System.out.println(b1);
    System.out.println(unsignedByteToInt(b1));
  }
  publicstaticint unsignedByteToInt(byte b) {
    return (int) b & 0xFF;
  }
}
```
