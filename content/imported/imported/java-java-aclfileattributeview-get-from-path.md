---
title: Java AclFileAttributeView get from Path
nav: Java AclFileAttributeView ...
description: AclFileAttributeView aclView = Files.getFileAttributeView(path,
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20210102121723/http://www.java2s.com/ref/java/java-aclfileattributeview-get-from-path.html
---
- java.nio.file.attribute
- java.nio.file.attribute AclEntry AclFileAttributeView BasicFileAttributeView DosFileAttributes FileOwnerAttributeView FileTime GroupPrincipal PosixFileAttributes PosixFileAttributeView PosixFilePermission UserDefinedFileAttributeView UserPrincipal UserPrincipalLookupService

## Description

Java AclFileAttributeView get from Path

```java title=Example.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclFileAttributeView;
import java.util.List;
import java.util.Set;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Path path = Paths.get("Main.java");

    AclFileAttributeView aclView = Files.getFileAttributeView(path,
        AclFileAttributeView.class);
    if (aclView == null) {
      System.out.println("ACL view is not supported.");
      return;/*fromwww.java2s.com*/
    }

    try {
      List<AclEntry> aclEntries = aclView.getAcl();
      for (AclEntry entry : aclEntries) {
        System.out.format("Principal: %s%n", entry.principal());
        System.out.format("Type: %s%n", entry.type());
        System.out.format("Permissions are:%n");

        Set<AclEntryPermission> permissions = entry.permissions();
        for (AclEntryPermission p : permissions) {
          System.out.format("%s %n", p);
        }

      }
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

PreviousNext

## Related

- Java WatchService watch file create, modify and delete events
- Java AclEntry get file flag and permissions
- Java AclFileAttributeView update
- Java AclFileAttributeView get permission and entry
- Java BasicFileAttributeView set file time
