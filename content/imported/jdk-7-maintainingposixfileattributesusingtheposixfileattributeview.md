---
title: Maintaining Posix file attributes using the PosixFileAttributeView
nav: Maintaining Posix file att...
description: Maintaining Posix file attributes using the PosixFileAttributeView
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20130820193046/http://java2s.com/Code/Java/JDK-7/MaintainingPosixfileattributesusingthePosixFileAttributeView.htm
---
Maintaining Posix file attributes using the PosixFileAttributeView

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.PosixFileAttributeView;
import java.nio.file.attribute.PosixFileAttributes;
import java.nio.file.attribute.PosixFilePermission;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("home/docs/users.txt");
    PosixFileAttributeView view = Files.getFileAttributeView(path,
        PosixFileAttributeView.class);
    PosixFileAttributes attributes = view.readAttributes();
    System.out.println("Group: " + attributes.group());
    System.out.println("Owner: " + attributes.owner().getName());
    Set<PosixFilePermission> permissions = attributes.permissions();
    for (PosixFilePermission permission : permissions) {
      System.out.print(permission.name() + " ");
    }
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
