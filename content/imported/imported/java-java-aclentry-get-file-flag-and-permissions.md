---
title: Java AclEntry get file flag and permissions
nav: Java AclEntry get file fla...
description: try {//fromwww.java2s.comAclFileAttributeView view = Files.getFileAttributeView(path, AclFileAttributeView.class);
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20210102121723/http://www.java2s.com/ref/java/java-aclentry-get-file-flag-and-permissions.html
---
- java.nio.file.attribute
- java.nio.file.attribute AclEntry AclFileAttributeView BasicFileAttributeView DosFileAttributes FileOwnerAttributeView FileTime GroupPrincipal PosixFileAttributes PosixFileAttributeView PosixFilePermission UserDefinedFileAttributeView UserPrincipal UserPrincipalLookupService

## Description

Java AclEntry get file flag and permissions

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
         displayAclEntries(aclEntryList);
      } catch (IOException ex) {
         ex.printStackTrace();
      }
   }

   privatestaticvoid displayAclEntries(List<AclEntry> aclEntryList) {
      System.out.println("ACL Entry List size: " + aclEntryList.size());
      for (AclEntry entry : aclEntryList) {
         System.out.println("User Principal Name: " + entry.principal().getName());
         System.out.println("ACL Entry Type: " + entry.type());
         displayEntryFlags(entry.flags());
         displayPermissions(entry.permissions());
         System.out.println();
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

- Java SimpleFileVisitor delete Directory
- Java SimpleFileVisitor traverse file systems
- Java WatchService watch file create, modify and delete events
- Java AclFileAttributeView update
- Java AclFileAttributeView get from Path
