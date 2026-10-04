---
title: Set group Principal
nav: Set group Principal
description: private static void setGroupPrincipal(Path path, String userName,
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20130820190439/http://java2s.com/Code/Java/JDK-7/SetgroupPrincipal.htm
---
Set group Principal

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.GroupPrincipal;
import java.nio.file.attribute.PosixFileAttributeView;
import java.nio.file.attribute.PosixFileAttributes;
import java.nio.file.attribute.UserPrincipal;
import java.nio.file.attribute.UserPrincipalLookupService;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("home/docs/users.txt");
    setGroupPrincipal(path, "A", "B");
  }
  private static void setGroupPrincipal(Path path, String userName,
      String groupName) throws Exception {
    System.out.println("Setting owner for " + path.getFileName());
    PosixFileAttributeView view = Files.getFileAttributeView(path,
        PosixFileAttributeView.class);
    PosixFileAttributes attributes = view.readAttributes();
    System.out.println("Old Group: " + attributes.group().getName());
    System.out.println("Old Owner: " + attributes.owner().getName());
    UserPrincipalLookupService lookupService = FileSystems.getDefault()
        .getUserPrincipalLookupService();
    UserPrincipal userPrincipal = lookupService.lookupPrincipalByName(userName);
    GroupPrincipal groupPrincipal = lookupService
        .lookupPrincipalByGroupName(groupName);
    view.setGroup(groupPrincipal);
    view.setOwner(userPrincipal);
    attributes = view.readAttributes();
    System.out.println("New Group: " + attributes.group().getName());
    System.out.println("New Owner: " + attributes.owner().getName());
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
15.  Set ACL
16.  Setting Owner
17.  Using setOwner
18.  Use FileTime
19.  Read attributes
20.  Using PosixFileAttributes
21.  Read BasicFileAttributes
