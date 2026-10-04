---
title: Java AclFileAttributeView get permission and entry
nav: Java AclFileAttributeView ...
description: try {//fromwww.java2s.comAclFileAttributeView view = Files.getFileAttributeView(path, AclFileAttributeView.class);
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20210102121723/http://www.java2s.com/ref/java/java-aclfileattributeview-get-permission-and-entry.html
---
- java.nio.file.attribute
- java.nio.file.attribute AclEntry AclFileAttributeView BasicFileAttributeView DosFileAttributes FileOwnerAttributeView FileTime GroupPrincipal PosixFileAttributes PosixFileAttributeView PosixFilePermission UserDefinedFileAttributeView UserPrincipal UserPrincipalLookupService

## Description

```java title=Example.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryFlag;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclFileAttributeView;
import java.util.List;
import java.util.Set;

publicclass Main {

   publicstaticvoid main(String[] args) {
      Path path = Paths.get("Main.java");
      try {//fromwww.java2s.comAclFileAttributeView view = Files.getFileAttributeView(path, AclFileAttributeView.class);
         List<AclEntry> aclEntryList = view.getAcl();
         for (AclEntry entry : aclEntryList) {
            System.out.println("User Principal Name: " + entry.principal().getName());
            System.out.println("ACL Entry Type: " + entry.type());
            displayEntryFlags(entry.flags());
            displayPermissions(entry.permissions());
            System.out.println();
         }
      } catch (IOException e) {
         e.printStackTrace();
      }

   }

   privatestaticvoid displayPermissions(Set<AclEntryPermission> permissionSet) {
      if (permissionSet.isEmpty()) {
         System.out.println("No Permissions present");
      } else {
         System.out.println("Permissions");
         for (AclEntryPermission permission : permissionSet) {
            System.out.print(permission.name() + " ");
         }
         System.out.println();
      }
   }

   privatestaticvoid displayEntryFlags(Set<AclEntryFlag> flagSet) {
      if (flagSet.isEmpty()) {
         System.out.println("No ACL Entry Flags present");
      } else {
         System.out.println("ACL Entry Flags");
         for (AclEntryFlag flag : flagSet) {
            System.out.print(flag.name() + " ");
         }
         System.out.println();
      }
   }
}
```

PreviousNext

## Related

- Java AclEntry get file flag and permissions
- Java AclFileAttributeView update
- Java AclFileAttributeView get from Path
