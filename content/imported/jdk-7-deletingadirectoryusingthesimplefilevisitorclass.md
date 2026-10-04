---
title: Deleting a directory using the SimpleFileVisitor class
nav: Deleting a directory using...
description: public FileVisitResult visitFile(Path file, BasicFileAttributes attributes)
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20130820232724/http://java2s.com/Code/Java/JDK-7/DeletingadirectoryusingtheSimpleFileVisitorclass.htm
---
```java title=Example.java
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
class DeleteDirectory extends SimpleFileVisitor<Path> {
  @Override
  public FileVisitResult visitFile(Path file, BasicFileAttributes attributes)
      throws IOException {
    System.out.println("Deleting " + file.getFileName());
    Files.delete(file);
    return FileVisitResult.CONTINUE;
  }
  @Override
  public FileVisitResult postVisitDirectory(Path directory,
      IOException exception) throws IOException {
    if (exception == null) {
      System.out.println("Deleting " + directory.getFileName());
      Files.delete(directory);
      return FileVisitResult.CONTINUE;
    } else {
      throw exception;
    }
  }
}
public class Test {
  public static void main(String[] args) {
    try {
      Files.walkFileTree(Paths.get("/home"), new DeleteDirectory());
    } catch (IOException ex) {
      ex.printStackTrace();
    }
  }
}
```

1.  List all Java file recursively with SimpleFileVisitor
---  ---
2.  Copying a directory using the SimpleFileVisitor class
3.  Using the SimpleFileVisitor class to traverse file systems
