---
title: Using the clipboard
nav: Using the clipboard
description: // This example is from the book _Java AWT Reference_ by John Zukowski.
section: Imported - java2s Archive
order: 1927
source: https://web.archive.org/web/20140829082242/http://www.java2s.com/Tutorial/Java/0120__Development/Usingtheclipboard.htm
---
```java title=Example.java
// This example is from the book _Java AWT Reference_ by John Zukowski.
// Written by John Zukowski.  Copyright (c) 1997 O'Reilly & Associates.
// You may study, use, modify, and distribute this example for any purpose.
// This example is provided WITHOUT WARRANTY either expressed or
import java.awt.Button;
import java.awt.Event;
import java.awt.Frame;
import java.awt.Panel;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.Transferable;
public class ClipMe extends Frame {
  TextField tf;
  TextArea ta;
  Button copy, paste;
  Clipboard clipboard = null;
  ClipMe() {
    super("Clipping Example");
    add(tf = new TextField("Welcome"), "North");
    add(ta = new TextArea(), "Center");
    ta.setEditable(false);
    Panel p = new Panel();
    p.add(copy = new Button("Copy"));
    p.add(paste = new Button("Paste"));
    add(p, "South");
    setSize(250, 250);
  }
  public static void main(String args[]) {
    new ClipMe().show();
  }
  public boolean handleEvent(Event e) {
    if (e.id == Event.WINDOW_DESTROY) {
      System.exit(0);
      return true; // never gets here
    }
    return super.handleEvent(e);
  }
  public boolean action(Event e, Object o) {
    if (clipboard == null)
      clipboard = getToolkit().getSystemClipboard();
    if ((e.target == tf) || (e.target == copy)) {
      StringSelection data;
      data = new StringSelection(tf.getText());
      clipboard.setContents(data, data);
    } else if (e.target == paste) {
      Transferable clipData = clipboard.getContents(this);
      String s;
      try {
        s = (String) (clipData.getTransferData(DataFlavor.stringFlavor));
      } catch (Exception ee) {
        s = ee.toString();
      }
      ta.setText(s);
    }
    return true;
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
