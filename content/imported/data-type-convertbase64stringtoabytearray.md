---
title: Convert base64 string to a byte array
nav: Convert base64 string to a...
description: Imported from the java2s.com archive: Convert base64 string to a byte array
section: Imported - java2s Archive
order: 1396
source: https://web.archive.org/web/20140829090053/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertbase64stringtoabytearray.htm
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

| 2.36.1. | Number Parsing |
|---|---|
| 2.36.2. | Integer.valueOf: Converting String to Integer |
| 2.36.3. | Integer.parseInt(): Converting String to int |
| 2.36.4. | String.ValueOf |
| 2.36.5. | sums a list of numbers entered by the user |
| 2.36.6. | Convert string of time to time object |
| 2.36.7. | Converting a String to a byte Number |
| 2.36.8. | Converting a String to a short Number |
| 2.36.9. | Converting a String to a int(integer) Number |
| 2.36.10. | Convert a String to Date |
| 2.36.11. | Convert String to character array |
| 2.36.12. | Convert base64 string to a byte array |
| 2.36.13. | Parse basic types |
