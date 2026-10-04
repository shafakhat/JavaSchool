---
title: ACL Attribute
nav: ACL Attribute
description: System.out.println("User Principal Name: " + entry.principal().getName());
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20130820180619/http://java2s.com/Code/Java/JDK-7/ACLAttribute.htm
---
ACL Attribute

```java title=Example.java
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryFlag;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclFileAttributeView;
import java.nio.file.attribute.GroupPrincipal;
import java.nio.file.attribute.UserPrincipal;
import java.nio.file.attribute.UserPrincipalLookupService;
import java.util.List;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("C:/home/docs/users.txt");
    AclFileAttributeView view = Files.getFileAttributeView(path,
        AclFileAttributeView.class);
    List<AclEntry> aclEntryList = view.getAcl();
    for (AclEntry entry : aclEntryList) {
      System.out.println("User Principal Name: " + entry.principal().getName());
      System.out.println("ACL Entry Type: " + entry.type());
      displayEntryFlags(entry.flags());
      displayPermissions(entry.permissions());
      System.out.println();
    }
  }
  private static void displayPermissions(Set<AclEntryPermission> permissionSet) {
    if (permissionSet.isEmpty()) {
      System.out.println("No Permissions present");
    } else {
      System.out.println("Permissions");
      for (AclEntryPermission permission : permissionSet) {
        System.out.println(permission.name() + " ");
      }
    }
  }
  private static void displayEntryFlags(Set<AclEntryFlag> flagSet) {
    if (flagSet.isEmpty()) {
      System.out.println("No ACL Entry Flags present");
    } else {
      System.out.println("ACL Entry Flags");
      for (AclEntryFlag flag : flagSet) {
        System.out.println(flag.name() + " ");
      }
    }
  }
}
```

1.  File metadata and DosFileAttributeView
---  ---
2.  Create PosixFilePermissions from string rwxr-x---
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
