---
title: Converting Between a BitSet and a Byte Array
nav: Converting Between a BitSe...
description: if ((bytes[bytes.length - i / 8 - 1] & (1 << (i % 8))) > 0) {
section: Imported - java2s Archive
order: 1068
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/ConvertingBetweenaBitSetandaByteArray.htm
---
```java title=Example.java
import java.util.BitSet;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
     System.out.println(fromByteArray(newbyte[]{1,2,3}));
  }
  // Returns a bitset containing the values in bytes.
publicstatic BitSet fromByteArray(byte[] bytes) {
    BitSet bits = new BitSet();
    for (int i = 0; i < bytes.length * 8; i++) {
      if ((bytes[bytes.length - i / 8 - 1] & (1 << (i % 8))) > 0) {
        bits.set(i);
      }
    }
    return bits;
  }
}
//{0, 1, 9, 16}
```
