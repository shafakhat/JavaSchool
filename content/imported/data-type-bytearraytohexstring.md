---
title: byte Array To Hex String
nav: byte Array To Hex String
description: Imported from the java2s.com archive: byte Array To Hex String
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/byteArrayToHexString.htm
---
```java title=Example.java
public class Main {
  public static void main(String arg[]) {
    byteArrayToHexString(("abc").getBytes());
  }
  public static String byteArrayToHexString(byte[] b) {
    StringBuffer sb = new StringBuffer(b.length * 2);
    for (int i = 0; i < b.length; i++) {
      int v = b[i] & 0xff;
      if (v < 16) {
        sb.append('0');
      }
      sb.append(Integer.toHexString(v));
    }
    return sb.toString().toUpperCase();
  }
}
```
