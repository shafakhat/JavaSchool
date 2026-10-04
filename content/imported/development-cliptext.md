---
title: Clip Text
nav: Clip Text
description: Clipboard clip = Toolkit.getDefaultToolkit().getSystemClipboard();
section: Imported - java2s Archive
order: 1936
source: https://web.archive.org/web/20140829083322/http://www.java2s.com/Tutorial/Java/0120__Development/ClipText.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.io.IOException;
import java.util.StringTokenizer;
public class MainClass {
  public static void main(String args[]) {
    // void copyToClipboard() {
    String toClipboard = "Hello from Java!";
    StringSelection ss = new StringSelection(toClipboard);
    Clipboard clip = Toolkit.getDefaultToolkit().getSystemClipboard();
    clip.setContents(ss, ss);
    // Paste
    clip = Toolkit.getDefaultToolkit().getSystemClipboard();
    Transferable contents = clip.getContents(new MainClass().getClass());
    if (contents == null)
      System.out.println("The clipboard is empty.");
    else {
      if (contents.isDataFlavorSupported(DataFlavor.stringFlavor)) {
        try {
          String data = (String) contents.getTransferData(DataFlavor.stringFlavor);
          if (data == null)
            System.out.println("null");
          else {
            StringTokenizer st = new StringTokenizer(data, "\n");
            while (st.hasMoreElements())
              System.out.println(st.nextToken());
          }
        } catch (IOException ex) {
          System.out.println("IOException");
        } catch (UnsupportedFlavorException ex) {
          System.out.println("UnsupportedFlavorException");
        }
      } else
        System.out.println("Wrong flavor.");
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
