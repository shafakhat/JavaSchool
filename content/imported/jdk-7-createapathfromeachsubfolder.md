---
title: Create a path from each sub folder
nav: Create a path from each su...
description: Path path = FileSystems.getDefault().getPath("/home/docs/status.txt");
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20130821095911/http://java2s.com/Code/Java/JDK-7/Createapathfromeachsubfolder.htm
---
Create a path from each sub folder

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) {
    Path path = FileSystems.getDefault().getPath("/home/docs/status.txt");
    path = Paths.get("/home", "docs", "users.txt");
    System.out.println("Absolute path: " + path.toAbsolutePath());
//  path = Paths.get("home", "docs", "users.txt");
//  System.out.println("Absolute path: " + path.toAbsolutePath());
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
7.  Get absolute path
8.  Get real path without following links
9.  Convert Path to File
10.  Get the relative path between two paths
11.  Creating a Path object using FileSystems
12.  Convert Path to String
13.  Get the file name from the Path object
14.  Get root from a Path Object
15.  Get the folder/directory for each part of a full path
16.  Get Subpath from a full path
17.  Is a path absolute
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
