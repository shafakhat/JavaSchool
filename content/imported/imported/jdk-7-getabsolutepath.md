---
title: Get absolute path
nav: Get absolute path
description: System.out.println("Absolute path: " + path.toAbsolutePath());
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20130821091221/http://java2s.com/Code/Java/JDK-7/Getabsolutepath.htm
---
```java title=Example.java
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path = Paths.get("users.txt");
    System.out.println("Absolute path: " + path.toAbsolutePath());
  }
}
```

1.  Create Path from URI
---  ---
2.  Combining paths using path resolution
3.  Get relative path
4.  Resolve sibling Path
5.  Converting a relative path into an absolute path
6.  Convert Path to URI
7.  Get real path without following links
8.  Convert Path to File
9.  Get the relative path between two paths
10.  Creating a Path object using FileSystems
11.  Convert Path to String
12.  Get the file name from the Path object
13.  Get root from a Path Object
14.  Get the folder/directory for each part of a full path
15.  Get Subpath from a full path
16.  Is a path absolute
17.  Create a path from each sub folder
18.  Catch Invalid path exception
19.  Determining whether two paths are equivalent with equals method
20.  Compare two path with compareTo and isSameFile method
21.  Managing symbolic links
22.  Check existance without following the symbolic links
23.  Removing redundancies by normalizing a path
24.  Get file Content Type
25.  Get file name from Path object
26.  Get the number of name element in a Path object
27.  Get parent Path
28.  Get the root path from the Path object
29.  Get the sub path from a Path object
30.  Get absolute path from a given Path
