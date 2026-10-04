---
title: Converting a relative path into an absolute path
nav: Converting a relative path...
description: Path path = Paths.get(new URI("file:///C:/home/docs/users.txt"));
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20130821051122/http://java2s.com/Code/Java/JDK-7/Convertingarelativepathintoanabsolutepath.htm
---
```java title=Example.java
import java.net.URI;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    String separator;
    separator = FileSystems.getDefault().getSeparator();
    System.out.println("The separator is " + separator);
    Path path = Paths.get(new URI("file:///C:/home/docs/users.txt"));
    System.out.println("subpath: " + path.subpath(0, 3));
    path = Paths.get("/home", "docs", "users.txt");
    System.out.println("Absolute path: " + path.toAbsolutePath());
    System.out.println("URI: " + path.toUri());
  }
}
```

1.  Create Path from URI
---  ---
2.  Combining paths using path resolution
3.  Get relative path
4.  Resolve sibling Path
5.  Convert Path to URI
6.  Get absolute path
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
