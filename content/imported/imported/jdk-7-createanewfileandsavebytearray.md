---
title: Create a new file and save byte array
nav: Create a new file and save...
description: Imported from the java2s.com archive: Create a new file and save byte array
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20130111100544/http://www.java2s.com:80/Code/Java/JDK-7/Createanewfileandsavebytearray.htm
---
Create a new file and save byte array

```java title=Example.java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
public class Test {
  public static void main(String[] args) throws IOException {
    Path path = Paths.get("/users.txt");
    byte[] contents = Files.readAllBytes(path);
    Path newPath = Paths.get("/newUsers.txt");
    Files.write(newPath, contents, StandardOpenOption.CREATE);
  }
}
```

1.  Read all file content to a byte array
---  ---
2.  Create new file and append byte array to it
3.  Reading all of the lines of a file returned as a list
4.  Create Directories with Files class
5.  Deleting File/Path
6.  Moving File
7.  Atomic File Move
8.  Resolve Sibling during file moving
9.  Moving a directory
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
