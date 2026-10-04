---
title: Java IO Tutorial - Java Paths
nav: Java IO Tutorial - Java Pa...
description: A Path object represents a path in a file system for a file, a directory, and a symbolic link.
section: Imported - java2s Archive
order: 50229
source: https://www.java2s.com/Tutorials/Java/Java_io/0970__Java_nio_Paths.html
---
```java title=Example.java
« Previous
```

- Next »

A Path object represents a path in a file system for a file, a directory, and a symbolic link.

Path is an interface in the java.nio.file package.

A path does not have to exist when we create a Path object.

Path can work with the old java.io.File apI. We can get a Path object from a File object using the method toPath() of the File class.

We can get a File object from a Path object using the toFile() method of a Path object.

We can perform two kinds of operations on a Path object:

- path operations
- file operations

We can use Path to access the components of a path such as the file name, root name, etc.

We can compare and examine paths. For example, checking if a path ends with .txt, comparing if two paths are identical, checking if a path is absolute or relative, etc. We can also combine and resolve paths.

We need to use the Files class to perform the file I/O operations on a Path object.

## Creating a Path Object

A FileSystem object acts as a factory to create a Path object.

getPath() method from FileSystem creates a Path object.

The following code creates a Path object for file path C:\Java_Dev\test1.txt on Windows:

```java title=Example.java

Path  p1  = FileSystems.getDefault().getPath("C:\\Java_Dev\\test1.txt");
```

We can pass components of a path separately to the getPath() method when constructing a Path object.

The following statement creates a Path object to represent the C:\Java_Dev\test1.txt path on Windows:

```java title=Example.java

Path  p2  = FileSystems.getDefault().getPath("C:", "Java_Dev",   "test1.txt");
```

Paths class can create a Path object from the components of a path string or a URI.

The Paths.get() static method creates a Path object.

The following creates Path objects to represent the same path, C:\Java_Dev\test1.txt:

```java title=Example.java

Path  p3  = Paths.get("C:\\Java_Dev\\test1.txt");
Path  p4  = Paths.get("C:", "Java_Dev", "test1.txt");
```

We can create a Path object from an empty path such as Paths.get(""). A Path object with an empty path refers to the default directory, which is the same as the current working directory.

## Components of a Path

A path in a file system consists of one or more components.

The getNameCount() method returns the number of components in a Path object excluding the root.

For example, the path C:\Java_Dev\test1.txt consists of three components: a root of C:, and two components named Java_Dev and test1.txt. In this case, the getNameCount() method will return 2.

The getName(int index) method returns the component name at the specified index. The component that is closest to the root has an index of 0.

The component that is farthest from the root has an index of count - 1. In the path.

C:\Java_Dev\test1.txt, the Java_Dev component has an index of 0 and the test1.txt component has an index of 1.

The getParent() method returns the parent of a path. If a path does not have a parent, it returns null.

The parent of the path C:\Java_Dev\test.txt is C:\Java_Dev.

The relative path test.txt has no parent.

The getRoot() method returns the root of the path. If a path does not have a root, it returns null.

For example, the path C:\Java_Dev\test1.txt on Windows has C:\ as its root.

The getFileName() method returns the file name denoted by the path.

If a path has no file name, it returns null. The file name is the farthest component from the root. For example, in the path C:\Java_Dev\test1.txt, test1.txt is the file name.

We can check if a path represents an absolute path by using the isAbsolute() method.

A path does not have to exist to get information about its components.

The following code shows how to access components of a Path object.

```java title=Example.java
import java.nio.file.Path;
import java.nio.file.Paths;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Path p1 = Paths.get("C:\\Java_Dev\\test1.txt");
    printDetails(p1);
    Path p2 = Paths.get("test1.txt");
    printDetails(p2);
  }
  publicstaticvoid printDetails(Path p) {
    System.out.println("Details for path: " + p);
    int count = p.getNameCount();
    System.out.println("Name count: " + count);
    for (int i = 0; i < count; i++) {
      Path name = p.getName(i);
      System.out.println("Name at  index   " + i + "  is " + name);
    }
    Path parent = p.getParent();
    Path root = p.getRoot();
    Path fileName = p.getFileName();
    System.out.println("Parent: " + parent + ", Root:   " + root
        + ", File Name: " + fileName);
    System.out.println("Absolute Path: " + p.isAbsolute());
  }
}
```

The code above generates the following result.

## Different Forms of a Path

We can get different type of representations for a path. Suppose we create a Path object as follows:

```java title=Example.java

Path  p1  = Paths.get("test.txt");
```

Here, p1 is a relative path. We can get the absolute path that is represented by p1 using its toAbsolutePath() method as follows:

```java title=Example.java

Path  p1AbsPath  = p1.toAbsolutePath();
```

Now the p1AbsPath is the absolute path for p1. For example, on Windows, p1AbsPath may look like C:\testapp\test.txt.

If a path is not an absolute path, the toAbsolutePath() method uses default directory to resolve the path.

If the path is an absolute path, the toAbsolutePath() method returns the same path.

We can use the toRealPath() method to get the real path of an existing file. It returns a canonical path to an existing file. If the path represents a symbolic link, it returns the real path of the target file.

We can pass a link option to this method indicating whether we want to follow the symbolic link to its target.

If the file represented by the path does not exist, the toRealPath() throws an IOException.

The following code shows how to get the real path from a Path object:

```java title=Example.java
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path p2 = Paths.get("test2.txt");
    // Follow link for p2, if it is a symbolic link
    Path p2RealPath = p2.toRealPath();
    System.out.println("p2RealPath:" + p2RealPath);
    Path p3 = Paths.get("test3.txt");
    // Do not follow link for p3, if it is a symbolic link
    Path p3RealPath = p3.toRealPath(LinkOption.NOFOLLOW_LINKS);
    System.out.println("p3RealPath:" + p3RealPath);
  }
}
```

## Path URI

Use the toUri() method of Path to get its URI representation.

The following code shows how to get the URI form of a path.

```java title=Example.java
import java.nio.file.Path;
import java.nio.file.Paths;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path p2 = Paths.get("test2.txt");
    java.net.URI p2UriPath = p2.toUri();
    System.out.println("Absolute Path: " + p2.toAbsolutePath());
    System.out.println("URI Path: " + p2UriPath);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
