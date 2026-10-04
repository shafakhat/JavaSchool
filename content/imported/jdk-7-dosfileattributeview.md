---
title: Dos File Attribute View
nav: Dos File Attribute View
description: Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20130820210427/http://java2s.com/Code/Java/JDK-7/DosFileAttributeView.htm
---
Dos File Attribute View

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.attribute.DosFileAttributeView;
import java.nio.file.attribute.DosFileAttributes;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
    DosFileAttributeView view = Files.getFileAttributeView(path,
        DosFileAttributeView.class);
    DosFileAttributes attributes = view.readAttributes();
    System.out.println("isArchive: " + attributes.isArchive());
    System.out.println("isHidden: " + attributes.isHidden());
    System.out.println("isReadOnly: " + attributes.isReadOnly());
    System.out.println("isSystem: " + attributes.isSystem());
  }
}
```

1.  File metadata and DosFileAttributeView
---  ---
2.  Create PosixFilePermissions from string rwxr-x---
3.  ACL Attribute
4.  Basic File Attribute View
5.  Get Owner
6.  Get the UserPrincipalLookupService
7.  Maintaining Posix file attributes using the PosixFileAttributeView
8.  Maintaining user defined file attributes using the UserDefinedFileAttributeView
9.  Obtaining a Map of file attributes
10.  Obtaining a single attribute at a time using the getAttribute method
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
