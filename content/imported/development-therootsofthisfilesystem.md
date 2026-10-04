---
title: The roots of this filesystem
nav: The roots of this filesystem
description: Imported from the java2s.com archive: The roots of this filesystem
section: Imported - java2s Archive
order: 1875
source: https://web.archive.org/web/20140829080945/http://www.java2s.com/Tutorial/Java/0120__Development/Therootsofthisfilesystem.htm
---
```java title=Example.java
import java.io.File;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileSystemView;
public class MainClass {
  public static void main(String[] args) {
    JFileChooser chooser = new JFileChooser();
    FileSystemView view = chooser.getFileSystemView();
    System.out.println("The roots of this filesystem are: ");
    File[] roots = view.getRoots();
    for (int i = 0; i < roots.length; i++) {
      System.out.println("  " + roots[i]);
    }
  }
}
```

| 6.38.1. | Home Directory |
|---|---|
| 6.38.2. | Default Directory |
| 6.38.3. | The roots of this filesystem |
| 6.38.4. | Root list with File.listRoots() |
