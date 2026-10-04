---
title: Delete a file with Files class
nav: Delete a file with Files c...
description: Path newFile = FileSystems.getDefault().getPath("C:\\home\\docs\\users.txt");
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20130111095155/http://www.java2s.com:80/Code/Java/JDK-7/DeleteafilewithFilesclass.htm
---
Delete a file with Files class

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
public class Test {
  public static void main(String[] args) throws Exception {
    Path newFile = FileSystems.getDefault().getPath("C:\\home\\docs\\users.txt");
    Files.createFile(newFile);
    System.out.println("File created successfully!");
    Files.delete(newFile);
    System.out.println("File deleted successfully!");
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
11.  Create temp file and directory
12.  Copying File with Files.copy method
13.  Copying Symbolic Links
14.  Copy Directory
15.  Copying from an Input Stream
16.  Copying From and Output Stream
17.  Creating File/Path
18.  Creating new file with Files class
19.  Delete a Path with Files.delete
20.  Using buffered IO for files
21.  Writing to a file using the BufferedWriter class
22.  Un-buffered IO support in the Files class
