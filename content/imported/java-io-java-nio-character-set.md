---
title: Java IO Tutorial - Java Character Set
nav: Java IO Tutorial - Java Ch...
description: We can convert a Unicode character to a sequence of bytes and vice versa using an encoding scheme.
section: Imported - java2s Archive
order: 50224
source: https://www.java2s.com/Tutorials/Java/Java_io/0920__Java_nio_Character_Set.html
---
```java title=Example.java
```

We can convert a Unicode character to a sequence of bytes and vice versa using an encoding scheme.

The java.nio.charset package provides classes to encode/decode a CharBuffer to a ByteBuffer and vice versa.

An object of the Charset class represents the encoding scheme. The CharsetEncoder class performs the encoding. The CharsetDecoder class performs the decoding.

We can get an object of the Charset class using its forName() method by passing the name of the character set as its argument.

For simple encoding and decoding tasks, we can use the encode() and decode() methods of the Charset class.

The following code shows how to encode a sequence of characters in the string Hello stored in a character buffer and decode it using the UTF-8 encoding-scheme.

```java title=Example.java
Charset cs  = Charset.forName("UTF-8");
CharBuffer cb  = CharBuffer.wrap("Hello");
ByteBuffer encodedData   = cs.encode(cb);
CharBuffer decodedData   = cs.decode(encodedData);
```

CharsetEncoder and CharsetDecoder classes accept a chunk of input to be encoded or decoded.

The encode() and decode() methods of the Charset class return the encoded and decoded buffers to us.

The following code shows how to get encoder and decoder objects from a Charset object.

```java title=Example.java
Charset cs  = Charset.forName("UTF-8");
CharsetEncoder encoder = cs.newEncoder();
CharsetDecoder decoder = cs.newDecoder();
```

The following code demonstrates how to list all character sets supported by a JVM.

```java title=Example.java
import java.util.Map;
import java.nio.charset.Charset;
import java.util.Set;
publicclass Main {
  publicstatic void main(String[] args) {
    Map<String, Charset> map = Charset.availableCharsets();
    Set<String> keys = map.keySet();
    System.out.println("Available  Character Set  Count:   " + keys.size());
    for (String charsetName : keys) {
      System.out.println(charsetName);
    }
  }
}
```

## Byte Order

A byte order is useful only in a multi-byte value stored in a byte buffer. To know the byte order of our machine, use the nativeOrder() method of the ByteOrder class.

```java title=Example.java
import java.nio.ByteOrder;
publicclass Main {
  publicstatic void main(String args[]) {
    ByteOrder b = ByteOrder.nativeOrder();
    if (b.equals(ByteOrder.BIG_ENDIAN)) {
      System.out.println("Big endian");
    } else {
      System.out.println("Little  endian");
    }
  }
}
```

The following code demonstrates how to get and set byte order for a byte buffer.

We use the order() method from the ByteBuffer to get or set the byte order.

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
publicclass Main {
  publicstaticvoid main(String[] args) {
    ByteBuffer bb = ByteBuffer.allocate(2);
    System.out.println("Default  Byte  Order: " + bb.order());
    bb.putShort((short) 300);
    bb.flip();
    showByteOrder(bb);
    bb.clear();
    bb.order(ByteOrder.LITTLE_ENDIAN);
    bb.putShort((short) 300);
    bb.flip();
    showByteOrder(bb);
  }
  publicstaticvoid showByteOrder(ByteBuffer bb) {
    System.out.println("Byte  Order: " + bb.order());
    while (bb.hasRemaining()) {
      System.out.print(bb.get() + "    ");
    }
    System.out.println();
  }
}
```

The code above generates the following result.

- « Previous
