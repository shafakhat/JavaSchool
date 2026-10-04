---
title: Converting a Primitive Type Value to a String
nav: Converting a Primitive Typ...
description: Imported from the java2s.com archive: Converting a Primitive Type Value to a String
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertingaPrimitiveTypeValuetoaString.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
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
