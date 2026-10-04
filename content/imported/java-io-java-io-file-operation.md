---
title: Java IO Tutorial - Java File Operation
nav: Java IO Tutorial - Java Fi...
description: We can create a new file using the createNewFile() method of the File class:
section: Imported - java2s Archive
order: 50199
source: https://www.java2s.com/Tutorials/Java/Java_io/0020__Java_io_File_Operation.html
---
```java title=Example.java
```

## File Create

We can create a new file using the createNewFile() method of the File class:

```java title=Example.java
File dummyFile = new File("test.txt");
boolean fileCreated  = dummyFile.createNewFile();
```

The createNewFile() method creates a new, empty file if the file with the specified name does not already exist.

It returns true if the file is created successfully; otherwise, it returns false. The method throws an IOException if an I/O error occurs.

We can also create a temporary file in the default temporary file directory or a directory. To create a temporary file in the default temporary directory, use the createTempFile() static method of the File class, which accepts a prefix and a suffix to generate the temporary file name.

```java title=Example.java
File  tempFile = File.createTempFile("abc", ".txt");
```

## Folder Create

We can use the mkdir() or mkdirs() method to create a new directory.

The mkdir() method creates a directory only if the parent directories specified in the pathname already exists.

```java title=Example.java
File newDir  = new File("C:\\users\\home");
```

The newDir.mkdir() method will create the home directory only if the C:\users directory already exists.

The newDir.mkdirs() method will create the users directory if it does not exist in the C: drive, and it will create the home directory under the C:\users directory.

## File Delete

We need to use the delete() method of the File class to delete a file/directory.

A directory must be empty before we can delete it.

The method returns true if the file/directory is deleted; otherwise, it returns false.

We can also delay the deletion of a file until the JVM terminates by using the deleteOnExit() method.

This is useful if we create temporary files in your program that we want to delete when your program exits.

To delete the dummy.txt file immediately

```java title=Example.java
File dummyFile = new File("dummy.txt");
dummyFile.delete();
```

To delete the dummy.txt file when the JVM terminates

```java title=Example.java
File dummyFile = new File("dummy.txt");
dummyFile.deleteOnExit();
```

## File Rename

To rename a file, we can use the renameTo() method, which takes a File object to represent the new file:

```java title=Example.java
boolean fileRenamed = oldFile.renameTo(newFile);
```

Full source code

```java title=Example.java
import java.io.File;
publicclass Main {
  publicstaticvoid main(String[] argv) {
    // Rename old-dummy.txt to new_dummy.txt
File oldFile = newFile("old_dummy.txt");
    File newFile = newFile("new_dummy.txt");
    boolean fileRenamed = oldFile.renameTo(newFile);
    if (fileRenamed) {
      System.out.println(oldFile + "  renamed  to " + newFile);
    } else {
      System.out.println("Renaming " + oldFile + "  to " + newFile
          + "  failed.");
    }
  }
}
```

The renameTo() method returns true if renaming of the file succeeds; otherwise, it returns false.

We need to check the return value to make sure the renaming succeeded.

The code above generates the following result.

## Example

The File object is immutable. Once created, it always represents the same pathname. When we rename a file, the old File object still represents the original pathname.

A File object represents a pathname, not an actual file in a file system.

The following code shows how to do File Creating, Deleting, and Renaming.

```java title=Example.java
import java.io.File;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    File newFile = newFile("my_new_file.txt");
    printFileDetails(newFile);
    // Create a new file
boolean fileCreated = newFile.createNewFile();
    if (!fileCreated) {
      System.out.println(newFile + "  could   not  be  created.");
    }
    printFileDetails(newFile);
    // Delete the new file
    newFile.delete();
    System.out.println("After deleting the new file:");
    printFileDetails(newFile);
    // recreate the file
    newFile.createNewFile();
    printFileDetails(newFile);
    // Let's tell the JVM to delete this file on exit
    newFile.deleteOnExit();
    System.out.println("After  using deleteOnExit() method:");
    printFileDetails(newFile);
    // Create a new file and rename it
File firstFile = newFile("my_first_file.txt");
    File secondFile = newFile("my_second_file.txt");
    fileCreated = firstFile.createNewFile();
    if (fileCreated || firstFile.exists()) {
      printFileDetails(firstFile);
      printFileDetails(secondFile);
      boolean renamedFlag = firstFile.renameTo(secondFile);
      if (!renamedFlag) {
        System.out.println("Could not  rename  " + firstFile);
      }
      printFileDetails(firstFile);
      printFileDetails(secondFile);
    }
  }
  publicstaticvoid printFileDetails(File f) {
    System.out.println("Absolute Path: " + f.getAbsoluteFile());
    System.out.println("File exists:  " + f.exists());
  }
}
```

The code above generates the following result.

## File Attributes

The File class contains methods that let we get/set attributes of files and directories.

We can set a file as read-only, readable, writable, and executable using the setReadOnly(), setReadable(), setWritable(), and setExecutable() methods, respectively.

We can use the lastModified() and setLastModified() methods to get and set the last modified date and time of a file.

We can check if a file is hidden using the isHidden() method.

## Size of a File

We can get the size of a file in bytes using the length() method of the File class.

```java title=Example.java
File myFile  = new File("myfile.txt");
long  fileLength = myFile.length();
```

If a File object represents a non-existent file, the length() method returns zero.

The return type of the length() method is long, not int.

## Listing Files and Directories

We can get a list of the available root directories in a file system by using the listRoots() static method of the File class. It returns an array of File objects.

```java title=Example.java
File[] roots = File.listRoots();
```

The following code shows how to list All Available Root Directories.

```java title=Example.java
import java.io.File;
publicclass Main {
  publicstaticvoid main(String[] args) {
    File[] roots = File.listRoots();
    System.out.println("List  of  root directories:");
    for (File f : roots) {
      System.out.println(f.getPath());
    }
  }
}
```

We can list all files and directories in a directory by using the list() or listFiles() methods of the File class.

The list() method returns an array of String, whereas the listFiles() method returns an array of File.

We can also use a file filter with these methods to exclude some files and directories from the returned results.

The following code shows how to list All Files and Directories in a Directory.

```java title=Example.java
import java.io.File;
publicclass Main {
  publicstatic void main(String[] args) {
    // Change the dirPath value to list files from your directory
    String dirPath = "C:\\";
    File dir = new File(dirPath);
    File[] list = dir.listFiles();
    for (File f : list) {
      if (f.isFile()) {
        System.out.println(f.getPath() + "  (File)");
      } elseif (f.isDirectory()) {
        System.out.println(f.getPath() + "  (Directory)");
      }
    }
  }
}
```

The code above generates the following result.

## File Filter

To exclude all files from the list with an extension .SYS, we can do this by using a file filter that is represented by an instance of the functional interface FileFilter.

It contains an accept() method that takes the File being listed as an argument and returns true if the File should be listed. Returning false does not list the file.

The following code creates a file filter that will filter files with the extension .SYS.

```java title=Example.java
FileFilter filter = file ->  {
    if (file.isFile()) {
        String fileName   = file.getName().toLowerCase();
        if (fileName.endsWith(".sys"))  {
            return false;
        }
    }
    return true;
};
```

The following code creates two file filters-one filters only files and another only directories:

```java title=Example.java
// Filters only  files
FileFilter fileOnlyFilter = File::isFile;
// Filters only  directories
FileFilter  dirOnlyFilter = File::isDirectory;
```

The following code shows how to use FileFilter to Filter Files.

```java title=Example.java
import java.io.File;
import java.io.FileFilter;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String dirPath = "C:\\";
    File dir = newFile(dirPath);
    // Create a file filter to exclude any .SYS file
    FileFilter filter = file -> {
      if (file.isFile()) {
        String fileName = file.getName().toLowerCase();
        if (fileName.endsWith(".sys")) {
          return false;
        }
      }
      return true;
    };
    File[] list = dir.listFiles(filter);
    for (File f : list) {
      if (f.isFile()) {
        System.out.println(f.getPath() + "  (File)");
      } elseif (f.isDirectory()) {
        System.out.println(f.getPath() + "  (Directory)");
      }
    }
  }
}
```

The code above generates the following result.

- « Previous
