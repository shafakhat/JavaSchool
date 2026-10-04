---
title: Get the root path from the Path object
nav: Get the root path from the...
description: System.out.println("Root of Path [" + listing.getRoot() + "]");
section: Imported - java2s Archive
order: 1074
source: https://web.archive.org/web/20130821091935/http://java2s.com/Code/Java/JDK-7/GettherootpathfromthePathobject.htm
---
```java title=Example.java
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception{
    Path listing = Paths.get("/usr/bin/zip");
    System.out.println("Root of Path [" + listing.getRoot() + "]");
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
18.  Create a path from each sub folder
19.  Catch Invalid path exception
20.  Determining whether two paths are equivalent with equals method
21.  Compare two path with compareTo and isSameFile method
22.  Managing symbolic links
23.  Check existance without following the symbolic links
24.  Removing redundancies by normalizing a path
25.  Get file Content Type
26.  Get file name from Path object
27.  Get the number of name element in a Path object
28.  Get parent Path
29.  Get the sub path from a Path object
30.  Get absolute path from a given Path
