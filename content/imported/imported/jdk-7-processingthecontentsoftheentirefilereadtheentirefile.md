---
title: Processing the contents of the entire file, Read the entire file
nav: Processing the contents of...
description: Processing the contents of the entire file, Read the entire file
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20130821021311/http://java2s.com/Code/Java/JDK-7/ProcessingthecontentsoftheentirefileReadtheentirefile.htm
---
```java title=Example.java
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.SeekableByteChannel;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws IOException {
    Path path = Paths.get("/users.txt");
    try (SeekableByteChannel sbc = Files.newByteChannel(path)) {
      ByteBuffer buffer = ByteBuffer.allocate(1024);
      sbc.position(4);
      sbc.read(buffer);
      for (int i = 0; i < 5; i++) {
        System.out.print((char) buffer.get(i));
      }
      buffer.clear();
      sbc.position(0);
      sbc.read(buffer);
      for (int i = 0; i < 4; i++) {
        System.out.print((char) buffer.get(i));
      }
      sbc.position(0);
      buffer = ByteBuffer.allocate(1024);
      String encoding = System.getProperty("file.encoding");
      int numberOfBytesRead = sbc.read(buffer);
      System.out.println("Number of bytes read: " + numberOfBytesRead);
      while (numberOfBytesRead > 0) {
        buffer.rewind();
        System.out.print("[" + Charset.forName(encoding).decode(buffer) + "]");
        buffer.flip();
        numberOfBytesRead = sbc.read(buffer);
        System.out.println("\nNumber of bytes read: " + numberOfBytesRead);
      }
    }
  }
}
```

1.  Random access IO using the SeekableByteChannel
---  ---
2.  SeekableByteChannel from Files.newByteChannel
3.  Writing to a file using the SeekableByteChannel interface
