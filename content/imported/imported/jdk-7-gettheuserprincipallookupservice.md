---
title: Get the UserPrincipalLookupService
nav: Get the UserPrincipalLooku...
description: FileOwnerAttributeView view = Files.getFileAttributeView(path,
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20130820201654/http://java2s.com/Code/Java/JDK-7/GettheUserPrincipalLookupService.htm
---
```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.FileOwnerAttributeView;
import java.nio.file.attribute.UserPrincipal;
import java.nio.file.attribute.UserPrincipalLookupService;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("C:/home/docs/users.txt");
    FileOwnerAttributeView view = Files.getFileAttributeView(path,
        FileOwnerAttributeView.class);
    UserPrincipal userPrincipal = view.getOwner();
    UserPrincipalLookupService lookupService = FileSystems.getDefault().getUserPrincipalLookupService();
    userPrincipal = lookupService.lookupPrincipalByName("users");
    view.setOwner(userPrincipal);
    System.out.println("UserPrincipal set: " + userPrincipal.getName());
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
