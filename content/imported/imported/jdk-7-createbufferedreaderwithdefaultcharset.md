---
title: Create BufferedReader with default charset
nav: Create BufferedReader with...
description: try (BufferedReader inputReader = Files.newBufferedReader(path, Charset.defaultCharset())) {
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20130111100931/http://www.java2s.com:80/Code/Java/JDK-7/CreateBufferedReaderwithdefaultcharset.htm
---
```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) {
    Path path = null;
    try {
        path = Paths.get(new URI("file:///C:/home/docs/users.txt"));
    } catch (URISyntaxException e) {
        System.out.println("Bad URI");
    }
    try (BufferedReader inputReader = Files.newBufferedReader(path, Charset.defaultCharset())) {
        String inputLine;
        while ((inputLine = inputReader.readLine()) != null) {
            System.out.println(inputLine);
        }
    } catch (IOException ex) {
        ex.printStackTrace();
    }
  }
}
```

1.  Delete a file with Files and Paths
---  ---
2.  Create BufferReader from Files class
3.  Interoperability between java.io.File and java.nio.file.Files
4.  File Information
5.  Filtering a directory using globbing
6.  Get file last modified time for a path object by using Files class
7.  Get the file size
8.  Is file a symbolic link
9.  Is a path a directory
