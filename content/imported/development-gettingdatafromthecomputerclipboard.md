---
title: Getting data from the computer clipboard
nav: Getting data from the comp...
description: Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
section: Imported - java2s Archive
order: 1930
source: https://web.archive.org/web/20140829082527/http://www.java2s.com/Tutorial/Java/0120__Development/Gettingdatafromthecomputerclipboard.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
public class Main {
  public static void main(String[] args) throws Exception {
    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    Transferable tran = clipboard.getContents(null);
    if (tran != null && tran.isDataFlavorSupported(DataFlavor.stringFlavor)) {
      String clipboardContent = (String) tran.getTransferData(DataFlavor.stringFlavor);
      System.out.println(clipboardContent);
    }
  }
}
```

| 6.44.1. | Using the clipboard |
|---|---|
| 6.44.2. | Read Clipboard |
| 6.44.3. | Placing text on the computer clipboard |
| 6.44.4. | Getting data from the computer clipboard |
| 6.44.5. | Get string value from clipboard |
| 6.44.6. | Write a string to the system clipboard |
| 6.44.7. | Getting and Setting an Image on the System Clipboard |
| 6.44.8. | Setting an image on the clipboard with a custom Transferable object to hold the image |
| 6.44.9. | Determining When an Item Is No Longer on the System Clipboard |
| 6.44.10. | implements ClipboardOwner |
| 6.44.11. | Copying data to system clipboard |
| 6.44.12. | Clip Text |
