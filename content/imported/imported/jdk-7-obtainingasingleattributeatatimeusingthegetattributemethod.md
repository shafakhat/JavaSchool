---
title: Obtaining a single attribute at a time using the getAttribute method
nav: Obtaining a single attribu...
description: Obtaining a single attribute at a time using the getAttribute method
section: Imported - java2s Archive
order: 1108
source: https://web.archive.org/web/20130820191356/http://java2s.com/Code/Java/JDK-7/ObtainingasingleattributeatatimeusingthegetAttributemethod.htm
---
```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
    System.out.println(Files.getAttribute(path, "size"));
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
11.  List POSIX File attribute
12.  Set permission for Posix File
13.  Remove permission for Posix File
14.  Set group Principal
15.  Set ACL
16.  Setting Owner
17.  Using setOwner
18.  Use FileTime
19.  Read attributes
20.  Using PosixFileAttributes
21.  Read BasicFileAttributes
