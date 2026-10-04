---
title: Moving a directory
nav: Moving a directory
description: Imported from the java2s.com archive: Moving a directory
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/20130111100559/http://www.java2s.com:80/Code/Java/JDK-7/Movingadirectory.htm
---
```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception{
    Path sourceFile = Paths.get("C:/home/docs");
    Path destinationFile = Paths.get("C:/home/music/docs");
    Files.move(sourceFile, destinationFile);
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
10.  Create temp file and directory
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
