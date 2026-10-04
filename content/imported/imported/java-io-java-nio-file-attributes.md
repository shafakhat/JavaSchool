---
title: Java IO Tutorial - Java Files Attributes
nav: Java IO Tutorial - Java Fi...
description: Files class can access the commonly used attributes of a file.
section: Imported - java2s Archive
order: 50233
source: https://www.java2s.com/Tutorials/Java/Java_io/1000__Java_nio_File_Attributes.html
---
```java title=Example.java
« Previous
```

- Next »

Files class can access the commonly used attributes of a file.

Files.isHidden(Path p) method tests if a file is hidden.

The following methods in the Files class can access various types of commonly used attributes of a file.

```java title=Example.java

long size(Path)
boolean isHidden(Path path)
boolean isRegularFile(Path path, LinkOption... options)
boolean isDirectory(Path path, LinkOption... options)
boolean isSymbolicLink(Path path)
FileTime getLastModifiedTime(Path path, LinkOption... options)
```

## File Attributes

The java.nio.attribute package contains the attribute-related classes. It bundles the file attributes in the following six types of views.

BasicFileAttributeView manages the basic file attributes such as creation time, last access time, last modified time, size, file type (regular file, directory, symbolic link, or other), and file key (a unique number for a file). This view is supported on all platforms.

DosFileAttributeView extends the BasicFileAttributeView accesses the file attributes that are specific to DOS. It provides the support to check if a file is a hidden file, a system file, an archive file, and a read-only file. It is available only on the systems that support DOS such as Microsoft Windows.

POSIX stands for Portable Operating System Interface for UNIX. PosixFileAttributeView extends the BasicFileAttributeView and adds support for attributes that are available on the systems that support POSIX standards such as UNIX. It lets we manage owner, group, and [related access] permissions.

FileOwnerAttributeView manages the owner of a file.

ACL stands for Access Control List. AclFileAttributeView manages the ACL for a file.

UserDefinedFileAttributeView manages a set of user-defined attributes for a file. The name of an attribute is a String. The value of an attribute could be of any data type.

## File Attribute View Support

supportsFileAttributeView() method from the FileStore class tells whether a specific file attribute view is supported by a file store.

If the specified file attribute view is supported, it returns true; otherwise, it returns false.

The following code shows how to check for file attribute support.

```java title=Example.java
import java.nio.file.FileStore;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.PosixFileAttributeView;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("");
    FileStore fs = Files.getFileStore(path);
    // Check if POSIX file attribute is supported by the file store
boolean supported = fs
        .supportsFileAttributeView(PosixFileAttributeView.class);
    if (supported) {
      System.out.println("POSIX file attribute view  is supported.");
    } else {
      System.out.println("POSIX file attribute view  is not  supported.");
    }
  }
}
```

The code above generates the following result.

## Example

The following code shows how to check for Supported File Attribute Views by a File Store.

```java title=Example.java
import java.io.IOException;
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
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Path path = Paths.get("C:");
    try {
      FileStore fs = Files.getFileStore(path);
      printDetails(fs, AclFileAttributeView.class);
      printDetails(fs, BasicFileAttributeView.class);
      printDetails(fs, DosFileAttributeView.class);
      printDetails(fs, FileOwnerAttributeView.class);
      printDetails(fs, PosixFileAttributeView.class);
      printDetails(fs, UserDefinedFileAttributeView.class);
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }
  publicstaticvoid printDetails(FileStore fs,
      Class<? extends FileAttributeView> attribClass) {
    boolean supported = fs.supportsFileAttributeView(attribClass);
    System.out.format("%s is  supported: %s%n", attribClass.getSimpleName(),
        supported);
  }
}
```

The code above generates the following result.

## Reading and Updating File Attributes

To read or update one file attribute, use Files class.

Files class has the following two static methods to read and update a file attribute using the attribute name as a string:

```java title=Example.java

Object getAttribute(Path path, String attribute, LinkOption... options)
Path setAttribute(Path path, String attribute, Object value, LinkOption... options)
```

To read or update multiple attributes of a file, work with a specific file attribute view.

For most of the file attribute views, we have to work with two interfaces named as TypeAttributes and TypeAttributeView.

For the basic file attributes, we have the BasicFileAttributes and BasicFileAtrributeView interfaces.

The TypeAttributes reads the attributes. The TypeAttributeView reads/updates the attributes.

The following two methods of the Files class read the file attributes in a bulk.

```java title=Example.java

<A extends BasicFileAttributes> A readAttributes(Path path, Class<A> type, LinkOption... options)
Map<String,Object> readAttributes(Path path, String attributes, LinkOption... options)
```

The last argument of both methods specify how a symbolic link is handled. By default, if a file is a symbolic link, the attributes of the target of the symbolic link are read.

If we specify NOFOLLOW_LINKS as the option, the attributes of the symbolic link are read, not the attributes of its target.

The first readAttributes() method returns all file attributes of a specified type in an TypeAttributes object.

To create the Path object representing the path of the file

```java title=Example.java

Path  path   = Paths.get("C:\\Java_Dev\\test1.txt");
```

To Read the basic file attributes

```java title=Example.java

BasicFileAttributes bfa  = Files.readAttributes(path, BasicFileAttributes.class);
```

To Get the last modified time

```java title=Example.java

FileTime lastModifiedTime  = bfa.lastModifiedTime();
```

To Get the size of the file

```java title=Example.java

long  size = bfa.size();
```

The second readAttributes() method returns all or some of the attributes of a specific type.

The list of attributes to read is supplied in a string form. The string form of an attribute list uses the following syntax:

```java title=Example.java

view-name:comma-separated-attributes
```

The view-name is the name of the attribute view that we want to read, such as basic, posix, acl, etc.

If view-name is omitted, it defaults to basic. If view-name is present, it is followed by a colon.

We can read all attributes of a specific view type by specifying an asterisk as the attributes list. For example, we can specify "basic:*" or "*" to read all basic file attributes.

To read the size and the last modified time of the basic view, we would use

```java title=Example.java
"basic:size,lastModifiedTime"or"size,lastModifiedTime".
```

To read the owner attribute of a file using an ACL view, we would use a string "acl:owner".

To read all posix attributes of a file, we would use "posix:*".

The following code prints the size and the last modified time of the file C:\Java_Dev\test1.txt.

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Map;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("C:\\Java_Dev\\test1.txt");
    // Prepare the attribute list
    String attribList = "basic:size,lastModifiedTime";
    // Read the attributes
    Map<String, Object> attribs = Files.readAttributes(path, attribList);
    System.out.format("Size:%s, Last   Modified   Time:%s %n",
        attribs.get("size"), attribs.get("lastModifiedTime"));
  }
}
```

## Example 2

The following code reads the basic file attributes of the file C:\Java_Dev\test1.txt and prints some of them on the standard output.

```java title=Example.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Path path = Paths.get("C:\\Java_Dev\\test1.txt");
    try {
      BasicFileAttributes bfa = Files.readAttributes(path,
          BasicFileAttributes.class);
      System.out.format("Size:%s bytes %n", bfa.size());
      System.out.format("Creation Time:%s %n", bfa.creationTime());
      System.out.format("Last Access  Time:%s %n", bfa.lastAccessTime());
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

We can also read file attributes using a specific view object.

We can use the getFileAttributeView() method declared as follows of the Files class to get a specific attribute view. It returns null if the file attribute view is not available.

```java title=Example.java

<V extends FileAttributeView> V  getFileAttributeView(Path path,  Class<V> type, LinkOption... options)
```

After getting a view object of a specific view type, we can read all attributes of that view type using the view object's readAttributes() method.

## Example 3

The following code reads all basic attributes for C:\Java_Dev\test1.txt file using a basic view object:

```java title=Example.java

Path  path   = Paths.get("C:\\Java_Dev\\test1.txt");
BasicFileAttributeView bfv = Files.getFileAttributeView(path,  BasicFileAttributeView.class);
BasicFileAttributes bfa  = bfv.readAttributes();
```

The following code shows how to use the basic file attribute view to read and update basic file attributes.

```java title=Example.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributeView;
import java.nio.file.attribute.BasicFileAttributes;
import java.nio.file.attribute.FileTime;
import java.time.Instant;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    Path path = Paths.get("C:\\Java_Dev\\test1.txt");
    try {
      BasicFileAttributeView bfv = Files.getFileAttributeView(path,
          BasicFileAttributeView.class);
      BasicFileAttributes bfa = bfv.readAttributes();
      System.out.format("Size:%s bytes %n", bfa.size());
      System.out.format("Creation  Time:%s %n", bfa.creationTime());
      System.out.format("Last Access  Time:%s %n", bfa.lastAccessTime());
      FileTime newLastModifiedTime = null;
      FileTime newLastAccessTime = null;
      FileTime newCreateTime = FileTime.from(Instant.now());
      bfv.setTimes(newLastModifiedTime, newLastAccessTime, newCreateTime);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

- Next »
- « Previous
