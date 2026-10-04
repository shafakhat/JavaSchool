---
title: Basic File Attribute View
nav: Basic File Attribute View
description: Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20130820181533/http://java2s.com/Code/Java/JDK-7/BasicFileAttributeView.htm
---
Basic File Attribute View

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.attribute.BasicFileAttributeView;
import java.nio.file.attribute.BasicFileAttributes;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = FileSystems.getDefault().getPath("/home/docs/users.txt");
    // BasicFileAttributes attributes = Files.readAttributes(path,
    // BasicFileAttributes.class);
    BasicFileAttributeView view = Files.getFileAttributeView(path,
        BasicFileAttributeView.class);
    BasicFileAttributes attributes = view.readAttributes();
    System.out.println("Creation Time: " + attributes.creationTime());
    System.out.println("Last Accessed Time: " + attributes.lastAccessTime());
    System.out.println("Last Modified Time: " + attributes.lastModifiedTime());
    System.out.println("File Key: " + attributes.fileKey());
    System.out.println("Directory: " + attributes.isDirectory());
    System.out.println("Other Type of File: " + attributes.isOther());
    System.out.println("Regular File: " + attributes.isRegularFile());
    System.out.println("Symbolic File: " + attributes.isSymbolicLink());
    System.out.println("Size: " + attributes.size());
  }
}
```

1.  File metadata and DosFileAttributeView
---  ---
2.  Create PosixFilePermissions from string rwxr-x---
3.  ACL Attribute
4.  Dos File Attribute View
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
