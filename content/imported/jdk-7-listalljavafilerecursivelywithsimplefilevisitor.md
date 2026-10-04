---
title: List all Java file recursively with SimpleFileVisitor
nav: List all Java file recursi...
description: public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
section: Imported - java2s Archive
order: 1089
source: https://web.archive.org/web/20130820225554/http://java2s.com/Code/Java/JDK-7/ListallJavafilerecursivelywithSimpleFileVisitor.htm
---
```java title=Example.java
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;
public class Test {
  public static void main(String[] args) throws IOException {
    Path startingDir = Paths.get("/Users/java");
    Files.walkFileTree(startingDir, new FindJavaVisitor());
  }
}
class FindJavaVisitor extends SimpleFileVisitor<Path> {
  @Override
  public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
    if (file.toString().endsWith(".java")) {
      System.out.println(file.getFileName());
    }
    return FileVisitResult.CONTINUE;
  }
}
```

1.  Copying a directory using the SimpleFileVisitor class
---  ---
2.  Deleting a directory using the SimpleFileVisitor class
3.  Using the SimpleFileVisitor class to traverse file systems
