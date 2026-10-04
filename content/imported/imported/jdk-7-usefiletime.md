---
title: Use FileTime
nav: Use FileTime
description: BasicFileAttributeView view = Files.getFileAttributeView(path,
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/20130820181643/http://java2s.com/Code/Java/JDK-7/UseFileTime.htm
---
```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributeView;
import java.nio.file.attribute.BasicFileAttributes;
import java.nio.file.attribute.FileTime;
import java.util.Calendar;
public class Test {
  public static void main(String[] args) throws Exception{
    Path path = Paths.get("C:/home/docs/users.txt");
    BasicFileAttributeView view = Files.getFileAttributeView(path,
        BasicFileAttributeView.class);
    BasicFileAttributes attributes = view.readAttributes();
    FileTime lastModifedTime = attributes.lastModifiedTime();
    FileTime createTime = attributes.creationTime();
    long currentTime = Calendar.getInstance().getTimeInMillis();
    FileTime lastAccessTime = FileTime.fromMillis(currentTime);
    view.setTimes(lastModifedTime, lastAccessTime, createTime);
    System.out.println(attributes.lastAccessTime());
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
16.  Set ACL
17.  Setting Owner
18.  Using setOwner
19.  Read attributes
20.  Using PosixFileAttributes
21.  Read BasicFileAttributes
