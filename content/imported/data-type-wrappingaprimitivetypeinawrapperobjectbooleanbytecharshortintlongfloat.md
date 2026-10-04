---
title: Wrapping a Primitive Type in a Wrapper Object
nav: Wrapping a Primitive Type ...
description: Imported from the java2s.com archive: Wrapping a Primitive Type in a Wrapper Object
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/WrappingaPrimitiveTypeinaWrapperObjectbooleanbytecharshortintlongfloatdouble.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    Boolean refBoolean = new Boolean(true);
    boolean bool = refBoolean.booleanValue();
    Byte refByte = new Byte((byte) 123);
    byte b = refByte.byteValue();
    Character refChar = new Character('x');
    char c = refChar.charValue();
    Short refShort = new Short((short) 123);
    short s = refShort.shortValue();
    Integer refInt = newInteger(123);
    int i = refInt.intValue();
    Long refLong = new Long(123L);
    long l = refLong.longValue();
    Float refFloat = new Float(12.3F);
    float f = refFloat.floatValue();
    Double refDouble = new Double(12.3D);
    double d = refDouble.doubleValue();
  }
}
```
