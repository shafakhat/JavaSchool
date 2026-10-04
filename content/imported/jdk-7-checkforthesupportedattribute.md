---
title: Check for the supported attribute
nav: Check for the supported at...
description: + fileStore.supportsFileAttributeView(FileAttributeView.class));
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20130821021559/http://java2s.com/Code/Java/JDK-7/Checkforthesupportedattribute.htm
---
```java title=Example.java
import java.nio.file.FileStore;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclFileAttributeView;
import java.nio.file.attribute.BasicFileAttributeView;
import java.nio.file.attribute.DosFileAttributeView;
import java.nio.file.attribute.FileAttributeView;
import java.nio.file.attribute.FileOwnerAttributeView;
import java.nio.file.attribute.PosixFileAttributeView;
import java.nio.file.attribute.UserDefinedFileAttributeView;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("C:/home/docs/users.txt");
    FileStore fileStore = Files.getFileStore(path);
    System.out.println("FileAttributeView supported: "
        + fileStore.supportsFileAttributeView(FileAttributeView.class));
    System.out.println("BasicFileAttributeView supported: "
        + fileStore.supportsFileAttributeView(BasicFileAttributeView.class));
    System.out.println("FileOwnerAttributeView supported: "
        + fileStore.supportsFileAttributeView(FileOwnerAttributeView.class));
    System.out.println("AclFileAttributeView supported: "
        + fileStore.supportsFileAttributeView(AclFileAttributeView.class));
    System.out.println("PosixFileAttributeView supported: "
        + fileStore.supportsFileAttributeView(PosixFileAttributeView.class));
    System.out.println("UserDefinedFileAttributeView supported: "
        + fileStore
            .supportsFileAttributeView(UserDefinedFileAttributeView.class));
    System.out.println("DosFileAttributeView supported: "
        + fileStore.supportsFileAttributeView(DosFileAttributeView.class));
    System.out.println("FileAttributeView supported: "
        + fileStore.supportsFileAttributeView("file"));
    System.out.println("BasicFileAttributeView supported: "
        + fileStore.supportsFileAttributeView("basic"));
    System.out.println("FileOwnerAttributeView supported: "
        + fileStore.supportsFileAttributeView("owner"));
    System.out.println("AclFileAttributeView supported: "
        + fileStore.supportsFileAttributeView("acl"));
    System.out.println("PosixFileAttributeView supported: "
        + fileStore.supportsFileAttributeView("posix"));
    System.out.println("UserDefinedFileAttributeView supported: "
        + fileStore.supportsFileAttributeView("user"));
    System.out.println("DosFileAttributeView supported: "
        + fileStore.supportsFileAttributeView("dos"));
  }
}
```

1.  Getting FileStore information
