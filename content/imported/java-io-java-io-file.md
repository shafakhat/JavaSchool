---
title: Java IO Tutorial - Java File
nav: Java IO Tutorial - Java File
description: An object of the File class is an abstract representation of a pathname of a file or a directory.
section: Imported - java2s Archive
order: 50198
source: https://www.java2s.com/Tutorials/Java/Java_io/0010__Java_io_File.html
---
An object of the File class is an abstract representation of a pathname of a file or a directory.

## Create File

We can create a File object from

- A pathname
- A parent pathname and a child pathname
- A URI (uniform resource identifier)

We can use one of the following constructors of the File class to create a file:

```java title=Example.java
File(String pathname)
File(File parent, String child)
File(String parent, String child)
File(URI uri)
```

If we have a file pathname string of test.txt, we can create an abstract pathname as the following code.

```java title=Example.java
File dummyFile = new File("test.txt");
```

A file named test.txt does not have to exist to create a File object using this statement.

The dummyFile object represents an abstract pathname, which may or may not point to a real file in a file-system.

The File class has several methods to work with files and directories.

Using a File object, we can create a new file, delete an existing file, rename a file, change permissions on a file, and so on.

isFile() and isDirectory() from the File class tells whether a File object represents a file or a directory.

## Current Working Directory

The current working directory for a JVM is set depending on how we run the java command.

We can get the current working directory for the JVM by reading the user.dir system property as follows:

```java title=Example.java
String  workingDir = System.getProperty("user.dir");
```

Use the System.setProperty() method to change the current working directory.

```java title=Example.java
System.setProperty("user.dir", "C:\\myDir");
```

To specify C:\test as the user.dir system property value on Windows, we run our program like so:

```java title=Example.java
java -Duser.dir=C:\test your-java-class
```

## File's Existence

We can check if the abstract pathname of a File object exists using the exists() method of the File class.

```java title=Example.java
boolean fileExists = dummyFile.exists();
```

Full Source Code

```java title=Example.java
import java.io.File;
publicclass Main {
  publicstaticvoid main(String[] argv) {
    // Create a File object
File dummyFile = newFile("dummy.txt");
    // Check for the file's existence
boolean fileExists = dummyFile.exists();
    if (fileExists) {
      System.out.println("The dummy.txt  file exists.");
    } else {
      System.out.println("The dummy.txt  file does  not  exist.");
    }
  }
}
```

The code above generates the following result.

## Path

The absolute path identifies the file uniquely on a file system. A canonical path is the simplest path that uniquely identifies the file on a file system.

We can use the getAbsolutePath() and getCanonicalPath() methods to get the absolute and canonical paths represented by a File object, respectively.

```java title=Example.java
import java.io.File;
import java.io.IOException;
publicclass Main {
  publicstaticvoid main(String[] args) {
    printFilePath("dummy.txt");
    printFilePath(".." + File.separator + "notes.txt");
  }
  publicstaticvoid printFilePath(String pathname) {
    File f = newFile(pathname);
    System.out.println("File  Name: " + f.getName());
    System.out.println("File  exists: " + f.exists());
    System.out.println("Absolute Path: " + f.getAbsolutePath());
    try {
      System.out.println("Canonical Path: " + f.getCanonicalPath());
    }
    catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## File separator

Different operating systems use a different character to separate two parts in a pathname.

For example, Windows uses a backslash (\) as a name separator in a pathname, whereas UNIX uses a forward slash (/).

The File class defines a constant named separator Char, which is the system-dependent name separator character.

We can use the File.separator Char constant to get the name separator as a character.

The File.separator constant gives we the name separator as a String.

Using the name separator in your program will make your Java code work on different platforms.

- « Previous
