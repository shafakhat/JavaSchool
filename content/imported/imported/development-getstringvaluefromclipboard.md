---
title: Get string value from clipboard
nav: Get string value from clip...
description: Transferable t = Toolkit.getDefaultToolkit().getSystemClipboard().getContents(null);
section: Imported
order: 20031
source: http://java2s.com/Tutorial/Java/0120__Development/Getstringvaluefromclipboard.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
public class Main {
  public static void main(String[] argv) {
    System.out.println(getClipboard());
  }
  public static String getClipboard() {
    Transferable t = Toolkit.getDefaultToolkit().getSystemClipboard().getContents(null);
    try {
      if (t != null && t.isDataFlavorSupported(DataFlavor.stringFlavor)) {
        String text = (String) t.getTransferData(DataFlavor.stringFlavor);
        return text.trim();
      }
    } catch (Exception e) {
    }
    return "";
  }
}
```
