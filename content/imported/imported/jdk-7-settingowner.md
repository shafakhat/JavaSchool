---
title: Setting Owner
nav: Setting Owner
description: FileOwnerAttributeView view = Files.getFileAttributeView(path,
section: Imported - java2s Archive
order: 1128
source: https://web.archive.org/web/20130820205203/http://java2s.com/Code/Java/JDK-7/SettingOwner.htm
---
Setting Owner

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
    UserPrincipalLookupService lookupService = FileSystems.getDefault()
        .getUserPrincipalLookupService();
    UserPrincipal userPrincipal = lookupService.lookupPrincipalByName("mary");
    view.setOwner(userPrincipal);
    System.out.println("Owner: " + view.getOwner().getName());
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
17.  Using setOwner
18.  Use FileTime
19.  Read attributes
20.  Using PosixFileAttributes
21.  Read BasicFileAttributes
