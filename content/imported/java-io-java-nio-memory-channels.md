---
title: Java IO Tutorial - Java Memory Channels
nav: Java IO Tutorial - Java Me...
description: Another way to perform I/O on a file, is mapping a region of the file into physical memory and treating it as a memory array.
section: Imported - java2s Archive
order: 50226
source: https://www.java2s.com/Tutorials/Java/Java_io/0940__Java_nio_Memory_Channels.html
---
```java title=Example.java
```

Another way to perform I/O on a file, is mapping a region of the file into physical memory and treating it as a memory array.

We can use MappedByteBuffer to perform memory-mapped file I/O.

To use memory-mapped file I/O, get a FileChannel object for the file, and use the map() method of the FileChannel to get a MappedByteBuffer.

Read or write directly to the mapped byte buffer instead of using the read() or write() method of the FileChannel object.

When reading from the mapped byte buffer, we read from the file's region which has been mapped.

When writing to the mapped byte buffer, we write to the mapped region of the file.

To write data to the mapped byte buffer immediately to the storage device, we need to use the force() method of the mapped byte buffer.

We can map a region of a file in a read-only, read-write, or private mode.

In a read-only mode, we can only read from the mapped byte buffer.

In a read-write mode, we can read from as well as write to the mapped byte buffer.

The private mode is also called a copy-on-write mode. When multiple programs map the same region of a file, all programs share the same region of the file.

When a program modifies the mapped region, a separate copy of that region is created only for that program, which is its private copy. Any modification made to the private copy is not visible to other programs.

## Example

The following code maps the whole file test.txt in a read-only mode. It reads the file and displays the contents on the standard output.

```java title=Example.java
import java.io.FileInputStream;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
publicclass Main {
  publicstaticvoid main(String[] args)throws Exception {
    FileInputStream fis = new FileInputStream("test.txt");
    FileChannel fc = fis.getChannel();
    long startRegion = 0;
    long endRegion = fc.size();
    MappedByteBuffer mbb = fc.map(FileChannel.MapMode.READ_ONLY, startRegion,
        endRegion);
    while (mbb.hasRemaining()) {
      System.out.print((char) mbb.get());
    }
    fis.close();
  }
}
```

The code above generates the following result.

- « Previous
