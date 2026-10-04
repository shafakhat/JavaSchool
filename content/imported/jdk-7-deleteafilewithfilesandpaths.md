---
title: Delete a file with Files and Paths
nav: Delete a file with Files a...
description: 3. Interoperability between java.io.File and java.nio.file.Files
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20130111095519/http://www.java2s.com:80/Code/Java/JDK-7/DeleteafilewithFilesandPaths.htm
---
Delete a file with Files and Paths

```java title=Example.java
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception{
    Files.delete(Paths.get(new URI("file:///tmp.txt")));
  }
}
```

1.  Create BufferReader from Files class
---  ---
2.  Create BufferedReader with default charset
3.  Interoperability between java.io.File and java.nio.file.Files
4.  File Information
5.  Filtering a directory using globbing
6.  Get file last modified time for a path object by using Files class
7.  Get the file size
8.  Is file a symbolic link
9.  Is a path a directory
