---
title: Random access IO using the SeekableByteChannel
nav: Random access IO using the...
description: 2. Processing the contents of the entire file, Read the entire file
section: Imported - java2s Archive
order: 1112
source: https://web.archive.org/web/20130820234445/http://java2s.com/Code/Java/JDK-7/RandomaccessIOusingtheSeekableByteChannel.htm
---
Random access IO using the SeekableByteChannel

```java title=Example.java
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.SeekableByteChannel;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
public class Test {
  public static void main(String[] args) throws IOException {
    Path path = Paths.get("/users.txt");
    final String newLine = System.getProperty("line.separator");
    try (SeekableByteChannel sbc = Files.newByteChannel(path,
        StandardOpenOption.WRITE)) {
      ByteBuffer buffer;
      long position = sbc.size();
      sbc.position(position);
      System.out.println("Position: " + sbc.position());
      buffer = ByteBuffer.wrap((newLine + "asdf").getBytes());
      sbc.write(buffer);
      System.out.println("Position: " + sbc.position());
      buffer = ByteBuffer.wrap((newLine + "asdf").getBytes());
      sbc.write(buffer);
      System.out.println("Position: " + sbc.position());
    }
  }
}
```

1.  SeekableByteChannel from Files.newByteChannel
---  ---
2.  Processing the contents of the entire file, Read the entire file
3.  Writing to a file using the SeekableByteChannel interface
