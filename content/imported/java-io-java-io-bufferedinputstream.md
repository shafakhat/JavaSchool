---
title: Java IO Tutorial - Java BufferedInputStream
nav: Java IO Tutorial - Java Bu...
description: A BufferedInputStream adds functionality to an input stream by buffering the data.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_io/0110__Java_io_BufferedInputStream.html
---
A BufferedInputStream adds functionality to an input stream by buffering the data.

It maintains an internal buffer to store bytes read from the underlying input stream.

We create the buffer input stream as follows:

String srcFile = "test.txt"; BufferedInputStream bis = new BufferedInputStream(new FileInputStream(srcFile));

The following code shows how to read from a File Using a BufferedInputStream.

```java title=Example.java
import java.io.BufferedInputStream;
import java.io.FileInputStream;
public class Main {
  public static void main(String[] args) {
    String srcFile = "test.txt";
    try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream(
        srcFile))) {
      // Read one byte at a time and display it
 byte byteData;
      while ((byteData = (byte) bis.read()) != -1) {
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
