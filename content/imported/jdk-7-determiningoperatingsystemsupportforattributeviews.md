---
title: Determining operating system support for attribute views
nav: Determining operating syst...
description: Set<String> supportedViews = fileSystem.supportedFileAttributeViews();
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20130111101309/http://www.java2s.com:80/Code/Java/JDK-7/Determiningoperatingsystemsupportforattributeviews.htm
---
Determining operating system support for attribute views

```java title=Example.java
import java.nio.file.FileSystem;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Set;
public class Test {
  public static void main(String[] args) {
    Path path = Paths.get("C:/home/docs/users.txt");
    FileSystem fileSystem = path.getFileSystem();
    Set<String> supportedViews = fileSystem.supportedFileAttributeViews();
    for (String view : supportedViews) {
      System.out.println(view);
    }
  }
}
Output:
acl
basic
owner
user
dos
```

1.  Getting FileSystem Information
