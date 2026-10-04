---
title: Java IO Tutorial - Java Symbolic Links
nav: Java IO Tutorial - Java Sy...
description: A symbolic link contains a reference to another file or directory.
section: Imported - java2s Archive
order: 50231
source: https://www.java2s.com/Tutorials/Java/Java_io/0980__Java_nio_Symbolic_Links.html
---
```java title=Example.java
```

A symbolic link contains a reference to another file or directory.

The file referenced by a symbolic link is known as the target file for the symbolic link.

Operations on a symbolic link are transparent to the application. We can work with symbolic links using the java.nio.file.Files class.

isSymbolicLink(Path p) method checks if the file specified by the specified path is a symbolic link.

createSymbolicLink() method of the Files, which may not be supported on all platforms, creates a symbolic link.

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path existingFilePath = Paths.get("C:\\Java_Dev\\test1.txt");
    Path symLinkPath = Paths.get("C:\\test1_link.txt");
    Files.createSymbolicLink(symLinkPath, existingFilePath);
  }
}
```

The Java NIO API follows the symbolic link by default. We can specify whether we want to follow a symbolic link or not. The option not to follow a symbolic link is indicated by using the enum constant LinkOption. NOFOLLOW_LINKS.

The LinkOption enum is declared in the java.nio.file package. Methods supporting this option let we pass an argument of the LinkOption type.

We can use the createLink(Path newLink, Path existingPath) method of the Files class to create a hard link.

- « Previous
