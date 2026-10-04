---
title: Java Swing Tutorial - Java Desktop.print(File file)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Desktop.print(File file) method.
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Desktop/0200__Desktop.print_File_file_.htm
---
```java title=Example.java
Back to Desktop  ↑
```

## Syntax

Desktop.print(File file) has the following syntax.

```java title=Example.java
publicvoid print(File file)  throws IOException
```

## Example

In the following code shows how to use Desktop.print(File file) method.

```java title=Example.java
import java.awt.Desktop;
import java.io.File;
import java.io.IOException;
publicclass Main {
  publicstaticvoid main(String[] a) {
    try {
      Desktop desktop = null;
      if (Desktop.isDesktopSupported()) {
        desktop = Desktop.getDesktop();
      }
       desktop.print(newFile("c:\\a.txt"));
    } catch (IOException ioe) {
      ioe.printStackTrace();
    }
  }
}
```

- Back to Desktop ↑
