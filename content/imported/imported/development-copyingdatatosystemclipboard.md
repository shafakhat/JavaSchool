---
title: Copying data to system clipboard
nav: Copying data to system cli...
description: Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, null);
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20111105150651/http://java2s.com/Tutorial/Java/0120__Development/Copyingdatatosystemclipboard.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
public class Main {
  public static void main(String[] argv) throws Exception {
  }
  // This method writes a string to the system clipboard.
  public static void copyToSystemClipboard(String str) {
    StringSelection ss = new StringSelection(str);
    Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, null);
  }
}
```
