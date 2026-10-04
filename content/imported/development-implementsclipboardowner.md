---
title: implements ClipboardOwner
nav: implements ClipboardOwner
description: Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, owner);
section: Imported - java2s Archive
order: 1953
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0120__Development/implementsClipboardOwner.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.ClipboardOwner;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;
public class Main {
  public static void main(String[] argv) throws Exception {
    ClipboardOwner owner = new MyClipboardOwner();
    StringSelection ss = new StringSelection("A String");
    Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, owner);
  }
}
class MyClipboardOwner implements ClipboardOwner {
  public void lostOwnership(Clipboard clipboard, Transferable contents) {
    System.out.println("lost");
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
