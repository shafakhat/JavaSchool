---
title: Returns a byte array of at least length 1
nav: Returns a byte array of at...
description: Imported from the java2s.com archive: Returns a byte array of at least length 1
section: Imported - java2s Archive
order: 1167
source: https://web.archive.org/web/20140312132411/http://www.java2s.com/Tutorial/Java/0060__Operators/Returnsabytearrayofatleastlength1.htm
---
```java title=Example.java
import java.util.BitSet;
public class Main {
  public static void main(String[] argv) throws Exception {
    BitSet bitset = new BitSet();
    bitset.set(1);
    System.out.println(toByteArray(bitset));
  }
  public static byte[] toByteArray(BitSet bits) {
    byte[] bytes = new byte[bits.length() / 8 + 1];
    for (int i = 0; i < bits.length(); i++) {
      if (bits.get(i)) {
        bytes[bytes.length - i / 8 - 1] |= 1 << (i % 8);
      }
    }
    return bytes;
  }
}
```
