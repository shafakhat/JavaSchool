---
title: Read attributes
nav: Read attributes
description: 8. Maintaining Posix file attributes using the PosixFileAttributeView
section: Imported - java2s Archive
order: 1114
source: https://web.archive.org/web/20130820180835/http://java2s.com/Code/Java/JDK-7/Readattributes.htm
---
```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    Path zip = Paths.get("/usr/bin/zip");
    System.out.println(Files.readAttributes(zip, "*"));
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
20.  Using PosixFileAttributes
21.  Read BasicFileAttributes
