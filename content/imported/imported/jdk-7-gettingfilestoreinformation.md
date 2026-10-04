---
title: Getting FileStore information
nav: Getting FileStore informat...
description: Imported from the java2s.com archive: Getting FileStore information
section: Imported - java2s Archive
order: 1077
source: https://web.archive.org/web/20130821014031/http://java2s.com/Code/Java/JDK-7/GettingFileStoreinformation.htm
---
Getting FileStore information

```java title=Example.java
import java.nio.file.FileStore;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
public class Test {
  static final long kiloByte = 1024;
  public static void main(String[] args) throws Exception {
    FileSystem fileSystem = FileSystems.getDefault();
    for (FileStore fileStore : fileSystem.getFileStores()) {
      long totalSpace = fileStore.getTotalSpace() / kiloByte;
      long usedSpace = (fileStore.getTotalSpace() - fileStore
          .getUnallocatedSpace()) / kiloByte;
      long usableSpace = fileStore.getUsableSpace() / kiloByte;
      String name = fileStore.name();
      String type = fileStore.type();
      boolean readOnly = fileStore.isReadOnly();
    }
  }
}
```

1.  Check for the supported attribute
