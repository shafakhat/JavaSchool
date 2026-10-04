---
title: List POSIX File attribute
nav: List POSIX File attribute
description: private static void listPermissions(Path path) throws Exception {
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20130820193124/http://java2s.com/Code/Java/JDK-7/ListPOSIXFileattribute.htm
---
List POSIX File attribute

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
    listPermissions(path);
  }
  private static void listPermissions(Path path) throws Exception {
    System.out.println("Permission for " + path.getFileName());
    PosixFileAttributeView view = Files.getFileAttributeView(path,
        PosixFileAttributeView.class);
    PosixFileAttributes attributes = view.readAttributes();
    System.out.println("Group: " + attributes.group().getName());
    System.out.println("Owner: " + attributes.owner().getName());
    Set<PosixFilePermission> permissions = attributes.permissions();
    System.out.print("Permissions: ");
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
8.  Maintaining Posix file attributes using the PosixFileAttributeView
9.  Maintaining user defined file attributes using the UserDefinedFileAttributeView
10.  Obtaining a Map of file attributes
11.  Obtaining a single attribute at a time using the getAttribute method
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
