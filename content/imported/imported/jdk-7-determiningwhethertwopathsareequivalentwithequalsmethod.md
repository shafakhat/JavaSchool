---
title: Determining whether two paths are equivalent with equals method
nav: Determining whether two pa...
description: Determining whether two paths are equivalent with equals method
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20130821095438/http://java2s.com/Code/Java/JDK-7/Determiningwhethertwopathsareequivalentwithequalsmethod.htm
---
```java title=Example.java
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) {
    Path path1 = Paths.get("/home/docs/users.txt");
    Path path2 = Paths.get("/home/docs/users.txt");
    Path path3 = Paths.get("/home/music/A.mp3");
    testEquals(path1, path2);
    testEquals(path1, path3);
  }
  private static void testEquals(Path path1, Path path2) {
    if (path1.equals(path2)) {
      System.out.println("equal");
    } else {
      System.out.println("NOT equal");
    }
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
