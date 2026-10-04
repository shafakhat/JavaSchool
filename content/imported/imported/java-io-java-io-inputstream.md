---
title: Java IO Tutorial - Java InputStream
nav: Java IO Tutorial - Java In...
description: We have concrete classes of FileInputStream, ByteArrayInputStream, and PipedInputStream, FilterInputStream.
section: Imported - java2s Archive
order: 50200
source: https://www.java2s.com/Tutorials/Java/Java_io/0080__Java_io_InputStream.html
---
```java title=Example.java
« Previous
```

- Next »

The abstract base component is the InputStream class.

```java title=Example.java

InputStream
 +--FileInputStream
 +--ByteArrayInputStream
 +--PipedInputStream
 +--FilterInputStream
 +--BufferedInputStream
 +--PushbackInputStream
 +--DataInputStream
 +--ObjectInputStream
```

We have concrete classes of FileInputStream, ByteArrayInputStream, and PipedInputStream, FilterInputStream.

## Methods

The superclass InputStream contains the basic methods to read data from an input stream, which are supported by all concrete classes.

The basic operation on an input stream is to read data from it. Some important methods defined in the InputStream class are listed in the following table.

ID  Method/Description
---  ---
1  read() Reads one byte and returns the read byte as an int. It returns -1 when the end of the input stream is reached.
2  read(byte[] buffer) Reads maximum up to the length of the specified buffer. It returns the number of bytes read in the buffer. It returns -1 if the end of the input stream is reached.
3  read(byte[] buffer,int offset, int length) Reads maximum up to the specified length bytes. The data is written in the buffer starting from the offset index. It returns the number of bytes read or -1 if the end of the input stream is reached.
3  close() Closes the input stream
4  available() Returns the estimated number of bytes that can be read from this input stream without blocking.

- Next »
- « Previous
