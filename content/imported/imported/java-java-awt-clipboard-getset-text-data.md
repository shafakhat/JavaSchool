---
title: Java AWT Clipboard get/set text data
nav: Java AWT Clipboard get/set...
description: // Pack data as a string in a Transferable objectTransferable transferableData = newStringSelection("demo2s.com");
section: Imported
order: 20068
source: http://www.java2s.com/ref/java/java-awt-clipboard-getset-text-data.html
---
- java.awt.datatransfer
- java.awt.datatransfer Clipboard

## Description

Java AWT Clipboard get/set text data

```java title=Example.java
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;

import javax.swing.JOptionPane;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Toolkit toolkit = Toolkit.getDefaultToolkit();
    Clipboard clipboard = toolkit.getSystemClipboard();

    // Pack data as a string in a Transferable objectTransferable transferableData = newStringSelection("demo2s.com");
    clipboard.setContents(transferableData, null);

    Transferable data = clipboard.getContents(null);
    if (data != null && data.isDataFlavorSupported(DataFlavor.stringFlavor)) {
      try {//fromwww.java2s.comString text = (String) data.getTransferData(DataFlavor.stringFlavor);
        System.out.println(text);
      } catch (Exception e) {
        e.printStackTrace();
      }
    } else {
      toolkit.beep();
      JOptionPane.showMessageDialog(null, "No text in the system clipboard to paste");
    }
  }
}
```

PreviousNext

## Related

- Java AWT Toolkit get screen size and center window
- Java AWT Toolkit check supported window state
- Java AWT Toolkit add event listener by mask
- Java ActionEvent check event source
- Java ActionEvent get action command text
