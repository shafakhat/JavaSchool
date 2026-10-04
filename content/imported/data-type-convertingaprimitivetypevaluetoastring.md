---
title: Converting a Primitive Type Value to a String
nav: Converting a Primitive Typ...
description: Imported from the java2s.com archive: Converting a Primitive Type Value to a String
section: Imported - java2s Archive
order: 1430
source: https://web.archive.org/web/20140829083107/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertingaPrimitiveTypeValuetoaString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    // Use String.valueOf()
    String s = String.valueOf(true);
    s = String.valueOf((byte) 0x11);
    s = String.valueOf((byte) 0xFF);
    s = String.valueOf('a');
    s = String.valueOf((short) 123);
    s = String.valueOf(123);
    s = String.valueOf(123L);
    s = String.valueOf(1.23F);
    s = String.valueOf(1.23D);
    // Use +
    s = "" + true;
    s = "" + ((byte) 0x12);
    s = "" + ((byte) 0xFF);
    s = "" + 'a';
    s = "" + ((short) 123);
    s = "" + 111;
    s = "" + 111L;
    s = "" + 1.11F;
    s = "" + 1.11D;
  }
}
```

| 2.37.1. | Convert String to java int Example |
|---|---|
| 2.37.2. | Converting Integer to Hex String |
| 2.37.3. | Converting int to binary string |
| 2.37.4. | Convert int to Octal String |
| 2.37.5. | valueOf(): convert to String |
| 2.37.6. | Converting byte to String |
| 2.37.7. | Converting long to String |
| 2.37.8. | Converting int to String |
| 2.37.9. | Converting float to String |
| 2.37.10. | Converting double to String |
| 2.37.11. | Converting short to String |
| 2.37.12. | Converting Char array to String |
| 2.37.13. | Converting a Primitive Type Value to a String |
| 2.37.14. | Convert Characters to Lower Case |
| 2.37.15. | Convert Characters to Upper Case |
| 2.37.16. | Convert a byte array to base64 string |
