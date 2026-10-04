---
title: Is file a symbolic link
nav: Is file a symbolic link
description: 4. Interoperability between java.io.File and java.nio.file.Files
section: Imported - java2s Archive
order: 1085
source: https://web.archive.org/web/20130111094806/http://www.java2s.com:80/Code/Java/JDK-7/Isfileasymboliclink.htm
---
```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    Path zip = Paths.get("/usr/bin/zip");
    System.out.println(Files.isSymbolicLink(zip));
  }
}
```

1.  Delete a file with Files and Paths
---  ---
2.  Create BufferReader from Files class
3.  Create BufferedReader with default charset
4.  Interoperability between java.io.File and java.nio.file.Files
5.  File Information
6.  Filtering a directory using globbing
7.  Get file last modified time for a path object by using Files class
8.  Get the file size
9.  Is a path a directory
