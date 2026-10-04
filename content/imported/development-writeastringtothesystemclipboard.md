---
title: Write a string to the system clipboard
nav: Write a string to the syst...
description: Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, null);
section: Imported - java2s Archive
order: 1934
source: https://web.archive.org/web/20140829082117/http://www.java2s.com/Tutorial/Java/0120__Development/Writeastringtothesystemclipboard.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.StringSelection;
public class Main {
  public static void main(String[] argv) throws Exception {
    StringSelection ss = new StringSelection("str");
    Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, null);
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
