---
title: Java AclFileAttributeView update
nav: Java AclFileAttributeView ...
description: AclFileAttributeView aclView = Files.getFileAttributeView(path, AclFileAttributeView.class);
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20210102121723/http://www.java2s.com/ref/java/java-aclfileattributeview-update.html
---
- java.nio.file.attribute
- java.nio.file.attribute AclEntry AclFileAttributeView BasicFileAttributeView DosFileAttributes FileOwnerAttributeView FileTime GroupPrincipal PosixFileAttributes PosixFileAttributeView PosixFilePermission UserDefinedFileAttributeView UserPrincipal UserPrincipalLookupService

## Description

Java AclFileAttributeView update

```java title=Example.java
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclEntryType;
import java.nio.file.attribute.AclFileAttributeView;
import java.nio.file.attribute.UserPrincipal;
import java.util.EnumSet;
import java.util.List;
import java.util.Set;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Path path = Paths.get("Main.java");

    AclFileAttributeView aclView = Files.getFileAttributeView(path, AclFileAttributeView.class);
    if (aclView == null) {
      System.out.println("ACL view is not supported.");
      return;/*fromwww.java2s.com*/
    }

    try {
      UserPrincipal bRiceUser = FileSystems.getDefault().getUserPrincipalLookupService()
          .lookupPrincipalByName("yourName");

      // Prepare permissions setSet<AclEntryPermission> permissions = EnumSet.of(AclEntryPermission.READ_DATA, AclEntryPermission.WRITE_DATA);

      // Let us build an ACL entryAclEntry.Builder builder = AclEntry.newBuilder();
      builder.setPrincipal(bRiceUser);
      builder.setType(AclEntryType.ALLOW);
      builder.setPermissions(permissions);
      AclEntry newEntry = builder.build();

      // Get the ACL entry for the pathList<AclEntry> aclEntries = aclView.getAcl();

      aclEntries.add(newEntry);

      // Update the ACL entries
      aclView.setAcl(aclEntries);

      System.out.println("ACL entry added for yourName successfully");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

PreviousNext

## Related

- Java SimpleFileVisitor traverse file systems
- Java WatchService watch file create, modify and delete events
- Java AclEntry get file flag and permissions
- Java AclFileAttributeView get from Path
- Java AclFileAttributeView get permission and entry
