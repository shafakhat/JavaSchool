---
title: Filtering a directory using globbing
nav: Filtering a directory usin...
description: Path directory = Paths.get("C:/Program Files/Java/jdk1.7.0/bin");
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20130111094800/http://www.java2s.com:80/Code/Java/JDK-7/Filteringadirectoryusingglobbing.htm
---
```java title=Example.java
import java.io.IOException;
import java.nio.file.DirectoryIteratorException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) {
    Path directory = Paths.get("C:/Program Files/Java/jdk1.7.0/bin");
    try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(
        directory, "java*.exe")) {
      for (Path file : directoryStream) {
        System.out.println(file.getFileName());
      }
    } catch (IOException | DirectoryIteratorException ex) {
      ex.printStackTrace();
    }
  }
}
```

1.  Delete a file with Files and Paths
---  ---
2.  Create BufferReader from Files class
3.  Create BufferedReader with default charset
4.  Interoperability between java.io.File and java.nio.file.Files
5.  File Information
6.  Get file last modified time for a path object by using Files class
7.  Get the file size
8.  Is file a symbolic link
9.  Is a path a directory
