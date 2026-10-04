---
title: Java IO Tutorial - Java PushbackInputStream
nav: Java IO Tutorial - Java Pu...
description: A PushbackInputStream adds functionality to an input stream allowing us to push back the read bytes using its unread() method.
section: Imported - java2s Archive
order: 50203
source: https://www.java2s.com/Tutorials/Java/Java_io/0120__Java_io_PushbackInputStream.html
---
```java title=Example.java
```

A PushbackInputStream adds functionality to an input stream allowing us to push back the read bytes using its unread() method.

There are three versions of the unread() method. One lets us push back one byte and other two let us push back multiple bytes.

## Example

```java title=Example.java
import java.io.FileInputStream;
import java.io.PushbackInputStream;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String srcFile = "test.txt";
    try (PushbackInputStream pis = new PushbackInputStream(new FileInputStream(
        srcFile))) {
      byte byteData;
      while ((byteData = (byte) pis.read()) != -1) {
        System.out.print((char) byteData);
        pis.unread(byteData);
        // Reread the byte we unread
        byteData = (byte) pis.read();
        System.out.print((char) byteData);
      }
    } catch (Exception e2) {
      e2.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
