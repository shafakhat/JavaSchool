---
title: Set ACL
nav: Set ACL
description: private static void displayAclEntries(List<AclEntry> aclEntryList) {
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/20130820182012/http://java2s.com/Code/Java/JDK-7/SetACL.htm
---
Set ACL

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryFlag;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclFileAttributeView;
import java.util.List;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("C:/home/docs/users.txt");
    AclFileAttributeView view = Files.getFileAttributeView(path,
        AclFileAttributeView.class);
    List<AclEntry> aclEntryList = view.getAcl();
    displayAclEntries(aclEntryList);
  }
  private static void displayAclEntries(List<AclEntry> aclEntryList) {
    System.out.println("ACL Entry List size: " + aclEntryList.size());
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
      return;
    }
    for (AclEntryPermission permission : permissionSet) {
      System.out.print(permission.name() + " ");
    }
    System.out.println();
  }
  private static void displayEntryFlags(Set<AclEntryFlag> flagSet) {
    if (flagSet.isEmpty()) {
      return;
    }
    for (AclEntryFlag flag : flagSet) {
      System.out.print(flag.name() + " ");
    }
    System.out.println();
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
16.  Setting Owner
17.  Using setOwner
18.  Use FileTime
19.  Read attributes
20.  Using PosixFileAttributes
21.  Read BasicFileAttributes
