---
title: Interoperability between java.io.File and java.nio.file.Files
nav: Interoperability between j...
description: Interoperability between java.io.File and java.nio.file.Files
section: Imported - java2s Archive
order: 1082
source: https://web.archive.org/web/20130111100205/http://www.java2s.com:80/Code/Java/JDK-7/InteroperabilitybetweenjavaioFileandjavaniofileFiles.htm
---
```java title=Example.java
import java.io.File;
import java.net.URI;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get(new URI("file:///C:/home/docs/users.txt"));
    File file = new File("C:\\home\\docs\\users.txt");
    Path toPath = file.toPath();
    System.out.println(toPath.equals(path));
  }
}
```

1.  Delete a file with Files and Paths
---  ---
2.  Create BufferReader from Files class
3.  Create BufferedReader with default charset
4.  File Information
5.  Filtering a directory using globbing
6.  Get file last modified time for a path object by using Files class
7.  Get the file size
8.  Is file a symbolic link
9.  Is a path a directory
