---
title: Java IO Tutorial - Java Channels
nav: Java IO Tutorial - Java Ch...
description: A channel is an open connection between a data source and a Java program to perform I/O operations.
section: Imported - java2s Archive
order: 50225
source: https://www.java2s.com/Tutorials/Java/Java_io/0930__Java_nio_Channels.html
---
```java title=Example.java
```

A channel is an open connection between a data source and a Java program to perform I/O operations.

The Channel interface is in the java.nio.channels package.

Channel interface declares only two methods: close() and isOpen().

## Various Channels

A ReadableByteChannel is used to read data from a data source into a byte buffer using its read() method. A WritableByteChannel is used to write data from a byte buffer to a data sink using its write() method.

A ByteChannel is capable of both reading and writing byte data using its read() and write() methods, respectively.

A ScatteringByteChannel reads data from a data source into multiple byte buffers. It is useful to read data from a known file format or a similar data source, where data is supplied in some fixed-length headers followed by a variable length body.

A GatheringByteChannel writes out data from multiple byte buffers.

## Create Channels

To obtain a channel, create an object of InputStream and OutputStream using old ways of working with I/O using classes in the java.io package.

The Channels class in the java.nio.channels package is a utility class that has many static methods to convert streams into channels and vice versa.

The Channels class also provides methods to convert readers/writers to channels and vice versa.

For example, if we have an input stream object named myInputStream, we can obtain a ReadableByteChannel as follows:

```java title=Example.java
ReadableByteChannel rbc  = Channels.newChannel(myInputStream);
```

If we have a ReadableByteChannel named rbc, we can obtain the underlying InputStream object as follows:

```java title=Example.java
InputStream myInputStream  = Channels.newInputStream(rbc);
```

FileInputStream and FileOutputStream classes have a new method called getChannel() to return a FileChannel object.

A FileChannel is used to read and write data to a file.

The FileChannel object obtained from a FileInputStream is opened in a read-only mode.

```java title=Example.java
FileInputStream fis  = new FileInputStream("test1.txt");
FileChannel fcReadOnly  = fis.getChannel(); // A  read-only  channel
```

A FileChannel object obtained from a FileOutputStream object is opened in a write-only mode.

```java title=Example.java
FileOutputStream fos   = new FileOutputStream("test1.txt");
FileChannel  fcWriteOnly = fos.getChannel(); // A  write-only  channel
```

If we obtain a FileChannel from a RandomAccessFile, it is opened in a read-only, write-only, or read-write mode, depending on the way we create that RandomAccessFile object.

The following code obtains FileChannel objects for different kinds of file streams:

```java title=Example.java
// read-only mode
RandomAccessFile  raf1 = new RandomAccessFile("test1.txt", "r");
FileChannel  rafReadOnly = raf1.getChannel(); // A  read-only  channel
// read-write mode
RandomAccessFile  raf2 = new RandomAccessFile("test1.txt", "rw");
FileChannel rafReadWrite = raf2.getChannel(); // A  read-write channel
```

## Reading/Writing Files

A FileChannel object maintains a position variable as a buffer does.

The read() and write() methods for FileChannel come in two varieties: relative position read/write and absolute position read/write.

When we open a FileChannel, its position is set to 0, which is the beginning of the file.

When we read from a FileChannel using a relative read() method, its position is incremented by the number of bytes read.

An absolute position read from a FileChannel does not affect its position.

We can get the current value of the position of a FileChannel object using its position() method.

We can set its position to a new position using its position(int newPosition) method.

Channels are also AutoCloseable. If we use a try-with-resources statement to obtain a channel, the channel will be closed automatically, thus avoiding a need for we to call the close() method of the channel explicitly.

The following code reads text from a file named test1.txt.

```java title=Example.java
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
publicclass Main {
  publicstaticvoid main(String[] args) {
    File inputFile = newFile("test1.txt");
    if (!inputFile.exists()) {
      System.out.println("The input file " + inputFile.getAbsolutePath()
          + "  does  not  exist.");
      System.out.println("Aborted the   file reading process.");
      return;
    }
    try (FileChannel fileChannel = new FileInputStream(inputFile).getChannel()) {
      ByteBuffer buffer = ByteBuffer.allocate(1024);
      while (fileChannel.read(buffer) > 0) {
        buffer.flip();
        while (buffer.hasRemaining()) {
          byte b = buffer.get();
          System.out.print((char) b);
        }
        buffer.clear();
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Example

The following code shows how to write to a File Using a Buffer and a Channel.

```java title=Example.java
import java.io.File;
import java.nio.channels.FileChannel;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.io.FileOutputStream;
publicclass Main {
  publicstaticvoid main(String[] args) {
    File outputFile = newFile("test.txt");
    try (FileChannel fileChannel = new FileOutputStream(outputFile)
        .getChannel()) {
      String text = getText();
      byte[] byteData = text.toString().getBytes("UTF-8");
      ByteBuffer buffer = ByteBuffer.wrap(byteData);
      fileChannel.write(buffer);
    } catch (IOException e1) {
      e1.printStackTrace();
    }
  }
  publicstatic String getText() {
    String lineSeparator = System.getProperty("line.separator");
    StringBuilder sb = new StringBuilder();
    sb.append("test");
    sb.append(lineSeparator);
    sb.append("test");
    sb.append(lineSeparator);
    sb.append("test");
    sb.append(lineSeparator);
    sb.append("test");
    return sb.toString();
  }
}
```

## Copying Contents of a File

We can use buffers and channels to copy a file.

Get the FileChannel object for the source file and the destination file, and call the transferTo() method on the source FileChannel object or call the transferFrom() method on the destination FileChannel object.

The following code shows how to copy a file.

```java title=Example.java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.channels.FileChannel;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    FileChannel sourceChannel = new FileInputStream("sourceFile").getChannel();
    FileChannel sinkChannel = new FileOutputStream("newFile").getChannel();
    // Copy source file contents to the sink file
    sourceChannel.transferTo(0, sourceChannel.size(), sinkChannel);
  }
}
```

- « Previous
