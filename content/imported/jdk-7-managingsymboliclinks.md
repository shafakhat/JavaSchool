---
title: Managing symbolic links
nav: Managing symbolic links
description: System.out.println("Absolute path: " + path.toAbsolutePath());
section: Imported - java2s Archive
order: 1095
source: https://web.archive.org/web/20130821091701/http://java2s.com/Code/Java/JDK-7/Managingsymboliclinks.htm
---
Managing symbolic links

```java title=Example.java
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;
public class Test {
  public static void main(String[] args) throws Exception {
    Path path1 = Paths.get("/home/docs/users.txt");
    Path path2 = Paths.get("/home/music/users.txt");
    System.out.println(Files.isSymbolicLink(path1));
    System.out.println(Files.isSymbolicLink(path2));
    Path path = Paths.get(new URI("C:/home/./music/users.txt"));
    System.out.println("Normalized: " + path.normalize());
    System.out.println("Absolute path: " + path.toAbsolutePath());
    System.out.println("URI: " + path.toUri());
    System.out.println("toRealPath (Do not follow links): "+ path.toRealPath(LinkOption.NOFOLLOW_LINKS));
    System.out.println("toRealPath: " + path.toRealPath());
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
22.  Check existance without following the symbolic links
23.  Removing redundancies by normalizing a path
24.  Get file Content Type
25.  Get file name from Path object
26.  Get the number of name element in a Path object
27.  Get parent Path
28.  Get the root path from the Path object
29.  Get the sub path from a Path object
30.  Get absolute path from a given Path
