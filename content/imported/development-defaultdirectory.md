---
title: Default Directory
nav: Default Directory
description: System.out.println("The default directory is " + view.getDefaultDirectory());
section: Imported - java2s Archive
order: 1874
source: https://web.archive.org/web/20140829081444/http://www.java2s.com/Tutorial/Java/0120__Development/DefaultDirectory.htm
---
```java title=Example.java
import java.io.File;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileSystemView;
public class MainClass {
  public static void main(String[] args) {
    JFileChooser chooser = new JFileChooser();
    FileSystemView view = chooser.getFileSystemView();
    System.out.println("The default directory is " + view.getDefaultDirectory());
  }
}
```

| 6.38.1. | Home Directory |
|---|---|
| 6.38.2. | Default Directory |
| 6.38.3. | The roots of this filesystem |
| 6.38.4. | Root list with File.listRoots() |
