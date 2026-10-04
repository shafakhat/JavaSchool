---
title: Read Clipboard
nav: Read Clipboard
description: Clipboard clip = Toolkit.getDefaultToolkit().getSystemClipboard();
section: Imported - java2s Archive
order: 1928
source: https://web.archive.org/web/20140829082509/http://www.java2s.com/Tutorial/Java/0120__Development/ReadClipboard.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
import javax.swing.JFrame;
public class MainClass extends JFrame {
  public static void main(String args[]) {
    Clipboard clip = Toolkit.getDefaultToolkit().getSystemClipboard();
    System.out.println("Object Name: " + clip.getName());
    Transferable contents = clip.getContents(new MainClass().getClass());
    if (contents == null)
      System.out.println("\n\nThe clipboard is empty.");
    else {
      DataFlavor flavors[] = contents.getTransferDataFlavors();
      for (int i = 0; i < flavors.length; ++i) {
        System.out.println("\n\n Name: " + flavors[i].getHumanPresentableName());
        System.out.println("\n MIME Type: " + flavors[i].getMimeType());
        Class cl = flavors[i].getRepresentationClass();
        if (cl == null)
          System.out.println("null");
        else
          System.out.println(cl.getName());
      }
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
