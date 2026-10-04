---
title: Java IO Tutorial - Java OutputStream
nav: Java IO Tutorial - Java Ou...
description: There are three important methods defined in the abstract superclass OutputStream: write(), flush(), and close().
section: Imported - java2s Archive
order: 50205
source: https://www.java2s.com/Tutorials/Java/Java_io/0200__Java_io_OutputStream.html
---
```java title=Example.java
« Previous
```

- Next »

There are three important methods defined in the abstract superclass OutputStream: write(), flush(), and close().

```java title=Example.java

The write() method writes bytes to an output stream.
It has three versions allowsing us to write one byte or multiple bytes at a time.
The flush() method is used to flush any buffered bytes to the data sink.
The close() method closes the output stream.
```

To use the BufferedOutputStream decorator for better speed to write to a file, use the following statement:

```java title=Example.java

BufferedOutputStream bos  = new BufferedOutputStream(new FileOutputStream("your output file  path"));
```

To write data to a ByteArrayOutputStream, use

```java title=Example.java

ByteArrayOutputStream baos  = new ByteArrayOutputStream();
baos.write(buffer); // buffer is a  byte   array
```

- Next »
- « Previous
