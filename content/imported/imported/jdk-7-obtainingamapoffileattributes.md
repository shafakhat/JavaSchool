---
title: Obtaining a Map of file attributes
nav: Obtaining a Map of file at...
description: Map<String, Object> attrsMap = Files.readAttributes(path, "*");
section: Imported - java2s Archive
order: 1107
source: https://web.archive.org/web/20130820184437/http://java2s.com/Code/Java/JDK-7/ObtainingaMapoffileattributes.htm
---
Obtaining a Map of file attributes

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
import java.util.Set;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("/home/docs/users.txt");
    Map<String, Object> attrsMap = Files.readAttributes(path, "*");
    Set<String> keys = attrsMap.keySet();
    for (String attribute : keys) {
      System.out.println(attribute + ": " + Files.getAttribute(path, attribute));
    }
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
