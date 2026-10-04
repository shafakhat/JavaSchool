---
title: Getting and Setting an Image on the System Clipboard
nav: Getting and Setting an Ima...
description: Transferable t = Toolkit.getDefaultToolkit().getSystemClipboard().getContents(null);
section: Imported
order: 20037
source: http://java2s.com/Tutorial/Java/0120__Development/GettingandSettinganImageontheSystemClipboard.htm
---
```java title=Example.java
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
public class Main {
  public static void main(String[] argv) throws Exception {
    Transferable t = Toolkit.getDefaultToolkit().getSystemClipboard().getContents(null);
    if (t != null && t.isDataFlavorSupported(DataFlavor.imageFlavor)) {
      Image img = (Image) t.getTransferData(DataFlavor.imageFlavor);
    }
  }
}
```
