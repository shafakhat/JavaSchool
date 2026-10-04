---
title: Copying a directory using the SimpleFileVisitor class
nav: Copying a directory using ...
description: Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS),
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20130821022453/http://java2s.com/Code/Java/JDK-7/CopyingadirectoryusingtheSimpleFileVisitorclass.htm
---
Copying a directory using the SimpleFileVisitor class

```java title=Example.java
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.FileVisitOption;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.EnumSet;
public class Test {
  public static void main(String[] args) {
    try {
      Path source = Paths.get("/home");
      Path target = Paths.get("/backup");
      Files.walkFileTree(source, EnumSet.of(FileVisitOption.FOLLOW_LINKS),
          Integer.MAX_VALUE, new CopyDirectory(source, target));
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }
}
class CopyDirectory extends SimpleFileVisitor<Path> {
  private Path source;
  private Path target;
  public CopyDirectory(Path source, Path target) {
    this.source = source;
    this.target = target;
  }
  @Override
  public FileVisitResult visitFile(Path file, BasicFileAttributes attributes)
      throws IOException {
    System.out.println("Copying " + source.relativize(file));
    Files.copy(file, target.resolve(source.relativize(file)));
    return FileVisitResult.CONTINUE;
  }
  @Override
  public FileVisitResult preVisitDirectory(Path directory,
      BasicFileAttributes attributes) throws IOException {
    Path targetDirectory = target.resolve(source.relativize(directory));
    try {
      System.out.println("Copying " + source.relativize(directory));
      Files.copy(directory, targetDirectory);
    } catch (FileAlreadyExistsException e) {
      if (!Files.isDirectory(targetDirectory)) {
        throw e;
      }
    }
    return FileVisitResult.CONTINUE;
  }
}
```

1.  List all Java file recursively with SimpleFileVisitor
---  ---
2.  Deleting a directory using the SimpleFileVisitor class
3.  Using the SimpleFileVisitor class to traverse file systems
