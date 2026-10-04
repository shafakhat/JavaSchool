---
title: Get DirectoryStream from a Path with file name matcher
nav: Get DirectoryStream from a...
description: DirectoryStream<Path> stream = Files.newDirectoryStream(dir,"*.properties");
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20130821080551/http://java2s.com/Code/Java/JDK-7/GetDirectoryStreamfromaPathwithfilenamematcher.htm
---
```java title=Example.java
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception{
    Path dir = Paths.get("C:/workspace/java");
    DirectoryStream<Path> stream = Files.newDirectoryStream(dir,"*.properties");
      for (Path entry : stream) {
        System.out.println(entry.getFileName());
      }
  }
}
```

1.  Writing your own directory filter
---  ---
2.  Zip file system provider
3.  Using the DirectoryStream interface to process the contents of a directory
