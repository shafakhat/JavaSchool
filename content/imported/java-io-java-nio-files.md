---
title: Java IO Tutorial - Java Files
nav: Java IO Tutorial - Java Fi...
description: java.nio.file.Files consists of all static methods that let we perform most of the file operations on a Path object.
section: Imported - java2s Archive
order: 50232
source: https://www.java2s.com/Tutorials/Java/Java_io/0990__Java_nio_Files.html
---
```java title=Example.java
```

java.nio.file.Files consists of all static methods that let we perform most of the file operations on a Path object.

## Creating New Files

Files can create regular files, directories, symbolic links, and temporary files/ directories.

Most of the methods accept a varargs parameter of the FileAttribute type, which lets we specify the file attributes.

createFile() method creates a new regular file. The new file created, is empty.

The file creation fails if the file already exists, or the parent directory does not exist.

The following code shows how to create a new file.

```java title=Example.java
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Path p1 = Paths.get("test.txt");
    try {
      Files.createFile(p1);
      System.out.format("File created:  %s%n", p1.toRealPath());
    } catch (FileAlreadyExistsException e) {
      System.out.format("File %s  already exists.%n", p1.normalize());
    } catch (NoSuchFileException e) {
      System.out.format("Directory %s  does  not  exists.%n", p1.normalize()
          .getParent());
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Create Directory

createDirectory() and createDirectories() methods create a new directory.

If the parent directory does not exist, the createDirectory() method fails.

The createDirectories() method creates a non-existent parent directory.

The createTempDirectory() and createTempFile() methods create a temporary directory and a temporary file respectively.

The following code shows how to create temporary files and directories.

```java title=Example.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
      String dirPrefix = "KDir";
      Path tDir = Files.createTempDirectory(dirPrefix);
      System.out.println("Temp directory: " + tDir);
      String fPrefix = "Header_";
      String fSuffix = ".txt";
      Path tFile1 = Files.createTempFile(fPrefix, fSuffix);
      System.out.println("Temp file1: " + tFile1);
      Path p1 = Paths.get("C:\\temp");
      Path tFile2 = Files.createTempFile(p1, fPrefix, fSuffix);
      System.out.println("Temp file2: " + tFile2);
  }
}
```

A temporary file/directory is not automatically deleted. We may want to use the deleteOnExit() method of the java.io.File class to delete the file when the JVM exits.

```java title=Example.java
Path  tempFile = Files.createTempFile("myTempFile", ".txt");
tempFile.toFile().deleteOnExit();
```

The code above generates the following result.

## Deleting Files

delete(Path p) and deleteIfExists(Path p) from Files to delete a file, a directory, and a symbolic link.

delete() method throws an exception if the deletion fails.

deleteIfExists() method does not throw a NoSuchFileException if the file being deleted does not exist.

It returns true if it deletes the file. Otherwise, it returns false.

The following code shows how to delete a file and handle exceptions:

```java title=Example.java
import java.io.IOException;
import java.nio.file.DirectoryNotEmptyException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path p = Paths.get("C:\\Java_Dev\\test1.txt");
    try {
      Files.delete(p);
      System.out.println(p + "  deleted successfully.");
    } catch (NoSuchFileException e) {
      System.out.println(p + "  does  not  exist.");
    } catch (DirectoryNotEmptyException e) {
      System.out.println("Directory " + p + "  is not  empty.");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

## Existence of a File

Files class has two methods called exists(Path p, LinkOption... options) and notExists(Path p, LinkOption... options) to check for the existence and non-existence of a file, respectively.

## Copying Files

Files class copy(Path source, Path target, CopyOption... options) method can copy the specified source path to the specified target path.

If the specified source file is a symbolic link, the target of the symbolic link is copied, not the symbolic link.

If the specified source file is a directory, an empty directory at the target location is created without copying the contents of the directory.

We can specify one or more of the following copy options with the copy() method:

- StandardCopyOption.REPLACE_EXISTING
- StandardCopyOption.COPY_ATTRIBUTES
- LinkOption.NOFOLLOW_LINKS

We can specify the REPLACE_EXISTING option to replace the existing target file.

If the target file is a symbolic link and if it exists, the symbolic link is replaced by specifying the REPLACE_EXISTING option, not the target of the symbolic link.

The COPY_ATTRIBUTES option copies the attributes of the source file to the target file.

If the NOFOLLOW_LINKS option is used, the copy() method copies the symbolic link, not the target of the symbolic link.

The following code shows the use of the copy() method to copy a file. It handles the possible exceptions if the copy operation fails.

```java title=Example.java
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.DirectoryNotEmptyException;
importstatic java.nio.file.StandardCopyOption.REPLACE_EXISTING;
importstatic java.nio.file.StandardCopyOption.COPY_ATTRIBUTES;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Path source = Paths.get("C:\\Java_Dev\\test1.txt");
    Path target = Paths.get("C:\\Java_Dev\\test1_backup.txt");
    try {
      Path p = Files.copy(source, target, REPLACE_EXISTING, COPY_ATTRIBUTES);
      System.out.println(source + "  has  been  copied to " + p);
    } catch (FileAlreadyExistsException e) {
      System.out.println(target + "  already exists.");
    } catch (DirectoryNotEmptyException e) {
      System.out.println(target + "  is not  empty.");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

## Moving Files

move(Path source, Path target, CopyOption... options) method of the Files class moves or rename a file.

The move operation fails if the specified target file already exists.

We can specify the REPLACE_EXISTING option to replace the existing target file.

If the file to move is a symbolic link, it moves the symbolic link, not the target of the symbolic link.

The move() method can only be used to move an empty directory.

Apart from the REPLACE_EXISTING CopyOption, we can use the ATOMIC_MOVE as another CopyOption.

If the ATOMIC_MOVE option is used, it throws an AtomicMoveNotSupportedException if the file could not be moved atomically.

If ATOMIC_MOVE option is specified, all other options are ignored.

The following code shows how to move a file by handling possible exceptions:

```java title=Example.java
importstatic java.nio.file.StandardCopyOption.ATOMIC_MOVE;
import java.io.IOException;
import java.nio.file.AtomicMoveNotSupportedException;
import java.nio.file.DirectoryNotEmptyException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.Paths;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path source = Paths.get("C:\\Java_Dev\\test1.txt");
    Path target = Paths.get("C:\\Java_Dev\\dir2\\test1.txt");
    try {
      Path p = Files.move(source, target, ATOMIC_MOVE);
      System.out.println(source + "  has  been  moved to " + p);
    }catch (NoSuchFileException e) {
      System.out.println("Source/target does  not  exist.");
    } catch (FileAlreadyExistsException e) {
      System.out.println(target + "  already exists.  Move failed.");
    } catch (DirectoryNotEmptyException e) {
      System.out.println(target + "  is not  empty.  Move failed.");
    } catch (AtomicMoveNotSupportedException e) {
      System.out.println("Atomic move is not  supported. MOve  failed.");
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

The code above generates the following result.

- « Previous
