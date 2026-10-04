---
title: Performing Bitwise Operations on a Bit Vector
nav: Performing Bitwise Operati...
description: Imported from the java2s.com archive: Performing Bitwise Operations on a Bit Vector
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/PerformingBitwiseOperationsonaBitVector.htm
---
```java title=Example.java
import java.util.BitSet;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    // Create the bitset
    BitSet bits = new BitSet();
    // Set a bit on
    bits.set(2);
    // Retrieving the value of a bit
boolean b = bits.get(0);
    b = bits.get(2);
    // Clear a bit
    bits.clear(1);
    // Setting a range of bits
    BitSet bits2 = new BitSet();
    bits2.set(1, 4);
    // And'ing two bitsets
    bits.and(bits2);
    // Xor'ing two bitsets
    bits.xor(bits2);
    // Flip all bits in the bitset
    bits.flip(0, bits.length());
    // Andnot'ing two bitsets
    bits.andNot(bits2);
    // Or'ing two bitsets
    bits.or(bits2);
  }
}
```
