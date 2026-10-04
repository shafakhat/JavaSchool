---
title: Getting FileSystem Information
nav: Getting FileSystem Informa...
description: Iterable<Path> rootDirectories = fileSystem.getRootDirectories();
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20130111101701/http://www.java2s.com:80/Code/Java/JDK-7/GettingFileSystemInformation.htm
---
```java title=Example.java
import java.nio.file.FileStore;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.spi.FileSystemProvider;
public class Test {
  public static void main(String[] args) {
    FileSystem fileSystem = FileSystems.getDefault();
    FileSystemProvider provider = fileSystem.provider();
    System.out.println("Provider: " + provider.toString());
    System.out.println("Open: " + fileSystem.isOpen());
    System.out.println("Read Only: " + fileSystem.isReadOnly());
    Iterable<Path> rootDirectories = fileSystem.getRootDirectories();
    System.out.println();
    System.out.println("Root Directories");
    for (Path path : rootDirectories) {
      System.out.println(path);
    }
    Iterable<FileStore> fileStores = fileSystem.getFileStores();
    System.out.println();
    System.out.println("File Stores");
    for (FileStore fileStore : fileStores) {
      System.out.println(fileStore.name());
    }
  }
}
```

1.  Determining operating system support for attribute views
