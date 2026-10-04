---
title: File Information
nav: File Information
description: Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20130111101656/http://www.java2s.com:80/Code/Java/JDK-7/FileInformation.htm
---
File Information

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Path;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
    displayFileAttributes(path);
  }
  private static void displayFileAttributes(Path path) throws Exception {
    String format = "Exists: %s %n" + "notExists: %s %n" + "Directory: %s %n"
        + "Regular: %s %n" + "Executable: %s %n" + "Readable: %s %n"
        + "Writable: %s %n" + "Hidden: %s %n" + "Symbolic: %s %n"
        + "Last Modified Date: %s %n" + "Size: %s %n";
    System.out.printf(format, Files.exists(path, LinkOption.NOFOLLOW_LINKS),
        Files.notExists(path, LinkOption.NOFOLLOW_LINKS),
        Files.isDirectory(path, LinkOption.NOFOLLOW_LINKS),
        Files.isRegularFile(path, LinkOption.NOFOLLOW_LINKS),
        Files.isExecutable(path), Files.isReadable(path),
        Files.isWritable(path), Files.isHidden(path),
        Files.isSymbolicLink(path),
        Files.getLastModifiedTime(path, LinkOption.NOFOLLOW_LINKS),
        Files.size(path));
  }
}
```

1.  Delete a file with Files and Paths
---  ---
2.  Create BufferReader from Files class
3.  Create BufferedReader with default charset
4.  Interoperability between java.io.File and java.nio.file.Files
5.  Filtering a directory using globbing
6.  Get file last modified time for a path object by using Files class
7.  Get the file size
8.  Is file a symbolic link
9.  Is a path a directory
