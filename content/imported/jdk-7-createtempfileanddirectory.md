---
title: Create temp file and directory
nav: Create temp file and direc...
description: Path rootDirectory = FileSystems.getDefault().getPath("C:/home/docs");
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20130111100155/http://www.java2s.com:80/Code/Java/JDK-7/Createtempfileanddirectory.htm
---
Create temp file and directory

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
public class Test {
  public static void main(String[] args) throws Exception {
    Path rootDirectory = FileSystems.getDefault().getPath("C:/home/docs");
    Path tempDirectory = Files.createTempDirectory(rootDirectory, "");
    System.out.println("Temporary directory created successfully!");
    String dirPath = tempDirectory.toString();
    System.out.println(dirPath);
    Path tempFile = Files.createTempFile(tempDirectory, "", "");
    System.out.println("Temporary file created successfully!");
    String filePath = tempFile.toString();
    System.out.println(filePath);
  }
}
```

1.  Read all file content to a byte array
---  ---
2.  Create a new file and save byte array
3.  Create new file and append byte array to it
4.  Reading all of the lines of a file returned as a list
5.  Create Directories with Files class
6.  Deleting File/Path
7.  Moving File
8.  Atomic File Move
9.  Resolve Sibling during file moving
10.  Moving a directory
11.  Copying File with Files.copy method
12.  Copying Symbolic Links
13.  Copy Directory
14.  Copying from an Input Stream
15.  Copying From and Output Stream
16.  Creating File/Path
17.  Creating new file with Files class
18.  Delete a file with Files class
19.  Delete a Path with Files.delete
20.  Using buffered IO for files
21.  Writing to a file using the BufferedWriter class
22.  Un-buffered IO support in the Files class
