---
title: SeekableByteChannel from Files.newByteChannel
nav: SeekableByteChannel from F...
description: 2. Processing the contents of the entire file, Read the entire file
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/20130821004608/http://java2s.com/Code/Java/JDK-7/SeekableByteChannelfromFilesnewByteChannel.htm
---
SeekableByteChannel from Files.newByteChannel

```java title=Example.java
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.SeekableByteChannel;
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
    }
  }
}
```

1.  Random access IO using the SeekableByteChannel
---  ---
2.  Processing the contents of the entire file, Read the entire file
3.  Writing to a file using the SeekableByteChannel interface
