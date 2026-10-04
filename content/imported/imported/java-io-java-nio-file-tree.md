---
title: Java IO Tutorial - Java File Tree
nav: Java IO Tutorial - Java Fi...
description: FileVisitor API can recursively process all files and directories in a file tree.
section: Imported - java2s Archive
order: 50235
source: https://www.java2s.com/Tutorials/Java/Java_io/1020__Java_nio_File_Tree.html
---
```java title=Example.java
```

FileVisitor API can recursively process all files and directories in a file tree.

The FileVisitor API is useful when we want to perform some actions on all or some files or directories in a file tree.

SimpleFileVisitor class is a basic implementation of the FileVisitor interface.

SimpleFileVisitor class do not do anything when a file/directory is visited. We can inherit our file visitor class from the SimpleFileVisitor class and override only the methods that fit our needs.

The Methods of the FileVisitor Interface

ID  Meaning
---  ---
1  FileVisitResult preVisitDirectory(T dir, BasicFileAttributes attrs) is called once before visiting entries in a directory.
2  FileVisitResult postVisitDirectory(T dir, IOException exc) called after entries in a directory have been visited. If there was any exception thrown during the iteration of a directory, the exception object is passed to this method as the second argument. If the second argument to this method is null, there was no exception during the directory iteration.
2  FileVisitResult visitFile(T file, BasicFileAttributes attrs) called when a file in a directory is visited.
3  FileVisitResult visitFileFailed(T file, IOException exc) called when a file or directory could not be visited for any reason.

The following table lists Enum Constants of FileVisitResult and Their Descriptions

Enum Constant  Description
---  ---
CONTINUE  Continues processing
SKIP_SIBLINGS  Continues processing without visiting the siblings of the file or directory.
SKIP_SUBTREE  Continues processing without visiting entries in the directory.
TERMINATE  Terminates the file visiting process.

We do not need to write logic in all four methods of our file visitor class. To copy a directory, code preVisitDirectory() method to create a new directory and the visitFile() method to copy the file.

The following code shows how to Print the Names of Subdirectories and Files of a directory.

```java title=Example.java
importstatic java.nio.file.FileVisitResult.CONTINUE;
//fromwww.java2s.comimport java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Path startDir = Paths.get("");
    FileVisitor<Path> visitor = getFileVisitor();
    try {
      Files.walkFileTree(startDir, visitor);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
  publicstatic FileVisitor<Path> getFileVisitor() {
    class DirVisitor<Path> extends SimpleFileVisitor<Path> {
      @Override
      public FileVisitResult preVisitDirectory(Path dir,
          BasicFileAttributes attrs) {
        System.out.format("%s [Directory]%n", dir);
        return CONTINUE;
      }
      @Override
      public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
        System.out.format("%s [File,  Size: %s  bytes]%n", file, attrs.size());
        return CONTINUE;
      }
    }
    FileVisitor<Path> visitor = new DirVisitor<>();
    return visitor;
  }
}
```

The code above generates the following result.

## Example

The following code shows how to use the FileVisitor API to Delete a Directory Tree.

```java title=Example.java
importstatic java.nio.file.FileVisitResult.CONTINUE;
importstatic java.nio.file.FileVisitResult.TERMINATE;
/*www.java2s.com*/import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Path dirToDelete = Paths.get("DIR");
    FileVisitor<Path> visitor = getFileVisitor();
    try {
      Files.walkFileTree(dirToDelete, visitor);
    }
    catch (IOException e) {
      System.out.println(e.getMessage());
    }
  }
  publicstatic FileVisitor<Path> getFileVisitor() {
    class DeleteDirVisitor extends SimpleFileVisitor<Path> {
      @Override
      public FileVisitResult postVisitDirectory(Path dir, IOException e)
          throws IOException {
        FileVisitResult result = CONTINUE;
        if (e != null) {
          System.out.format("Error deleting  %s.  %s%n", dir, e.getMessage());
          result = TERMINATE;
        } else {
          Files.delete(dir);
          System.out.format("Deleted directory  %s%n", dir);
        }
        return result;
      }
      @Override
      public FileVisitResult visitFile(Path file, BasicFileAttributes attrs)
          throws IOException {
        Files.delete(file);
        System.out.format("Deleted file %s%n", file);
        return CONTINUE;
      }
    }
    FileVisitor<Path> visitor = new DeleteDirVisitor();
    return visitor;
  }
}
```

The code above generates the following result.

## Example 2

The following code shows how to use the walkFileTree() method to follow a symbolic link.

```java title=Example.java

import java.nio.file.FileVisitOption;
import java.nio.file.FileVisitor;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.EnumSet;
import java.util.Set;
import static  java.nio.file.FileVisitOption.FOLLOW_LINKS;
publicclass Main {
  publicstatic void main(String[] args) throws Exception {
    Path startDir = Paths.get("");
    FileVisitor<Path> visitor = create your visitor;
    Set<FileVisitOption> options = EnumSet.of(FOLLOW_LINKS);
    int depth = Integer.MAX_VALUE;
    Files.walkFileTree(startDir, options, depth, visitor);
  }
}
```

## Pattern matching

We can perform pattern matching on the string form of Path objects using the glob and regex patterns.

The functional interface PathMatcher is used to perform the match. It contains a method matches(Path path) method that returns true if the specified path matches the pattern.

The pattern string consists of two parts, syntax and pattern, separated by a colon:

```java title=Example.java

syntax:pattern
```

The value for syntax is either glob or regex. The pattern part follows the syntax that depends on the value of the syntax part.

The glob pattern uses the following syntax rules:

- * matches zero or more characters without crossing directory boundaries.
- ** match zero or more characters crossing directory boundaries.
- ? matches exactly one character.
- \ escapes the special meaning of the following character.
- \\ matches a single backslash
- \* matches an asterisk.

Characters placed inside brackets [] are called a bracket expression, which matches a single character. [aeiou] matches a, e, i, o, or u.

A dash between two characters specifies a range. [a-z] matches all alphabets between a and z.

The exclamation mark (!) after the left bracket is treated as negation. [!abc] matches all characters except a, b, and c.

Use a group of subpatterns by specifying comma-separated subpatterns inside braces ({}). For example, {txt, java, doc} matches txt, java, and doc.

The matching of the root component of a path is implementation-dependent.

The following code shows how to use a PathMatcher object to match a path against a glob pattern.

```java title=Example.java
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.PathMatcher;
import java.nio.file.Paths;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    String globPattern = "glob:**txt";
    PathMatcher matcher = FileSystems.getDefault().getPathMatcher(globPattern);
    Path path = Paths.get("C:\\Java_Dev\\test1.txt");
    boolean matched = matcher.matches(path);
    System.out.format("%s matches  %s:  %b%n", globPattern, path, matched);
  }
}
```

The code above generates the following result.

- « Previous
