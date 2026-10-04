---
title: Java IO Tutorial - Java FileSystem
nav: Java IO Tutorial - Java Fi...
description: Java 7 introduced New Input/Output 2 (NIO.2) API and provides a new I/O API.
section: Imported - java2s Archive
order: 50228
source: https://www.java2s.com/Tutorials/Java/Java_io/0960__Java_nio_FileSystem.html
---
```java title=Example.java
```

Java 7 introduced New Input/Output 2 (NIO.2) API and provides a new I/O API.

It adds three packages to the Java class library: java.nio.file, java.nio.file.attribute, and java.nio.file.spi.

## File System

An object of the FileSystem class represents a file system in a Java program.

A FileSystem object is used to perform two tasks:

- an interface between a Java program and a file system.
- a factory for creating many types of file system-related objects and services.

A FileSystem object is platform-dependent.

## Create FileSystem

To obtain the default FileSystem object, we need to use the getDefault() static method of the FileSystems class as follows:

```java title=Example.java
FileSystem fs  = FileSystems.getDefault();
```

A FileSystem consists of one or more FileStore. The getFileStores() method from FileSystem returns an Iterator for the FileStore objects.

The getRootDirectories() method from FileSystem returns an iterator of Path objects, which represent paths to all top-level directories.

isReadOnly() method from FileSystem tells if we get read-only access to the file stores.

## Example

The following code shows how to use a FileSystem object.

```java title=Example.java
import java.nio.file.FileStore;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.io.IOException;
publicclass Main {
  publicstaticvoid main(String[] args) {
    FileSystem fs = FileSystems.getDefault();
    System.out.println("Read-only file system: " + fs.isReadOnly());
    System.out.println("File name separator: " + fs.getSeparator());
    for (FileStore store : fs.getFileStores()) {
      printDetails(store);
    }
    for (Path root : fs.getRootDirectories()) {
      System.out.println(root);
    }
  }
  publicstaticvoid printDetails(FileStore store) {
    try {
      String desc = store.toString();
      String type = store.type();
      long totalSpace = store.getTotalSpace();
      long unallocatedSpace = store.getUnallocatedSpace();
      long availableSpace = store.getUsableSpace();
      System.out.println(desc + ", Total: " + totalSpace + ",  Unallocated: "
          + unallocatedSpace + ",  Available: " + availableSpace);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
