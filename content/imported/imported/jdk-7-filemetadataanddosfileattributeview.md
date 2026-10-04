---
title: File metadata and DosFileAttributeView
nav: File metadata and DosFileA...
description: System.out.println("Is Directory:" + Files.isDirectory(path));
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20130820180537/http://java2s.com/Code/Java/JDK-7/FilemetadataandDosFileAttributeView.htm
---
```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.attribute.DosFileAttributeView;
public class Test {
  public static void main(String[] args) throws Exception{
    Path path = FileSystems.getDefault().getPath("./file2.log");
    System.out.println("File Size:" + Files.size(path));
    System.out.println("Is Directory:" + Files.isDirectory(path));
    System.out.println("Is Regular File:" + Files.isRegularFile(path));
    System.out.println("Is Symbolic Link:" + Files.isSymbolicLink(path));
    System.out.println("Is Hidden:" + Files.isHidden(path));
    System.out.println("Last Modified Time:" + Files.getLastModifiedTime(path));
    System.out.println("Owner:" + Files.getOwner(path));
    DosFileAttributeView view = Files.getFileAttributeView(path,
        DosFileAttributeView.class);
    System.out.println("Archive  :" + view.readAttributes().isArchive());
    System.out.println("Hidden   :" + view.readAttributes().isHidden());
    System.out.println("Read-only:" + view.readAttributes().isReadOnly());
    System.out.println("System   :" + view.readAttributes().isSystem());
    view.setHidden(false);
  }
}
```

1.  Create PosixFilePermissions from string rwxr-x---
---  ---
2.  ACL Attribute
3.  Basic File Attribute View
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
