---
title: Placing text on the computer clipboard
nav: Placing text on the comput...
description: Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
section: Imported
order: 20074
source: http://java2s.com/Tutorial/Java/0120__Development/Placingtextonthecomputerclipboard.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
public class Main {
  public static void main(String[] args) {
    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    clipboard.setContents(new StringSelection("string"), null);
  }
}
```
