---
title: Read BasicFileAttributes
nav: Read BasicFileAttributes
description: 8. Maintaining Posix file attributes using the PosixFileAttributeView
section: Imported - java2s Archive
order: 1115
source: https://web.archive.org/web/20130820192947/http://java2s.com/Code/Java/JDK-7/ReadBasicFileAttributes.htm
---
```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
public class Test {
  public static void main(String[] args) throws Exception {
    Path file = Paths.get("/opt/platform/java");
    if (Files.isSymbolicLink(file)) {
      file = Files.readSymbolicLink(file);
    }
    Files.readAttributes(file, BasicFileAttributes.class);
  }
}
```

1.  File metadata and DosFileAttributeView
---  ---
2.  Create PosixFilePermissions from string rwxr-x---
3.  ACL Attribute
4.  Basic File Attribute View
5.  Dos File Attribute View
6.  Get Owner
7.  Get the UserPrincipalLookupService
8.  Maintaining Posix file attributes using the PosixFileAttributeView
9.  Maintaining user defined file attributes using the UserDefinedFileAttributeView
10.  Obtaining a Map of file attributes
11.  Obtaining a single attribute at a time using the getAttribute method
12.  List POSIX File attribute
13.  Set permission for Posix File
14.  Remove permission for Posix File
15.  Set group Principal
16.  Set ACL
17.  Setting Owner
18.  Using setOwner
19.  Use FileTime
20.  Read attributes
21.  Using PosixFileAttributes
