---
title: Create BufferReader from Files class
nav: Create BufferReader from F...
description: 3. Interoperability between java.io.File and java.nio.file.Files
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20130111100926/http://www.java2s.com:80/Code/Java/JDK-7/CreateBufferReaderfromFilesclass.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) {
    try (BufferedReader inputReader = Files.newBufferedReader(
        Paths.get(new URI("file:///C:/users.txt")),
        Charset.defaultCharset());
        BufferedWriter outputWriter = Files.newBufferedWriter(
            Paths.get(new URI("file:///C:/users.bak")),
            Charset.defaultCharset())) {
      String inputLine;
      while ((inputLine = inputReader.readLine()) != null) {
        outputWriter.write(inputLine);
        outputWriter.newLine();
      }
      System.out.println("Copy complete!");
    } catch (URISyntaxException | IOException ex) {
      ex.printStackTrace();
    }
  }
}
```

1.  Delete a file with Files and Paths
---  ---
2.  Create BufferedReader with default charset
3.  Interoperability between java.io.File and java.nio.file.Files
4.  File Information
5.  Filtering a directory using globbing
6.  Get file last modified time for a path object by using Files class
7.  Get the file size
8.  Is file a symbolic link
9.  Is a path a directory
