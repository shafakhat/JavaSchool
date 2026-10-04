---
title: Create PosixFilePermissions from string rwxr-x---
nav: Create PosixFilePermission...
description: Path directory = fileSystem.getPath("./newDirectoryWPermissions");
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20130820194946/http://java2s.com/Code/Java/JDK-7/CreatePosixFilePermissionsfromstringrwxrx.htm
---
Create PosixFilePermissions from string rwxr-x---

```java title=Example.java
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.attribute.FileAttribute;
import java.nio.file.attribute.PosixFilePermission;
import java.nio.file.attribute.PosixFilePermissions;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    FileSystem fileSystem = FileSystems.getDefault();
    Path directory = fileSystem.getPath("./newDirectoryWPermissions");
    Set<PosixFilePermission> perms = PosixFilePermissions
        .fromString("rwxr-x---");
    FileAttribute<Set<PosixFilePermission>> attr = PosixFilePermissions
        .asFileAttribute(perms);
    Files.createDirectory(directory, attr);
  }
}
```

1.  File metadata and DosFileAttributeView
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
