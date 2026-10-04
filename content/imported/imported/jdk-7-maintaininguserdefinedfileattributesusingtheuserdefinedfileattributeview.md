---
title: Maintaining user defined file attributes using the UserDefinedFileAttributeView
nav: Maintaining user defined f...
description: Maintaining user defined file attributes using the UserDefinedFileAttributeView
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20130820190817/http://java2s.com/Code/Java/JDK-7/MaintaininguserdefinedfileattributesusingtheUserDefinedFileAttributeView.htm
---
Maintaining user defined file attributes using the UserDefinedFileAttributeView

```java title=Example.java
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.UserDefinedFileAttributeView;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("C:/home/docs/users.txt");
    UserDefinedFileAttributeView view = Files.getFileAttributeView(path,
        UserDefinedFileAttributeView.class);
    view.write("publishable", Charset.defaultCharset().encode("true"));
    System.out.println("Publishable set");
    String name = "publishable";
    ByteBuffer buffer = ByteBuffer.allocate(view.size(name));
    view.read(name, buffer);
    buffer.flip();
    String value = Charset.defaultCharset().decode(buffer).toString();
    System.out.println(value);
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
9.  Obtaining a Map of file attributes
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
