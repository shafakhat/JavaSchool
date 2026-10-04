---
title: Using PosixFileAttributes
nav: Using PosixFileAttributes
description: import static java.nio.file.attribute.PosixFilePermission.GROUP_READ;
section: Imported - java2s Archive
order: 1145
source: https://web.archive.org/web/20130820182109/http://java2s.com/Code/Java/JDK-7/UsingPosixFileAttributes.htm
---
Using PosixFileAttributes

```java title=Example.java
import static java.nio.file.attribute.PosixFilePermission.GROUP_READ;
import static java.nio.file.attribute.PosixFilePermission.OWNER_READ;
import static java.nio.file.attribute.PosixFilePermission.OWNER_WRITE;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.PosixFileAttributes;
import java.nio.file.attribute.PosixFilePermission;
import java.nio.file.attribute.PosixFilePermissions;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    Path profile = Paths.get("/user/Admin/.profile");
    PosixFileAttributes attrs = Files.readAttributes(profile,
        PosixFileAttributes.class);
    Set<PosixFilePermission> posixPermissions = attrs.permissions();
    posixPermissions.clear();
    String owner = attrs.owner().getName();
    String perms = PosixFilePermissions.toString(posixPermissions);
    System.out.format("%s %s%n", owner, perms);
    posixPermissions.add(OWNER_READ);
    posixPermissions.add(GROUP_READ);
    posixPermissions.add(OWNER_READ);
    posixPermissions.add(OWNER_WRITE);
    Files.setPosixFilePermissions(profile, posixPermissions);
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
21.  Read BasicFileAttributes
