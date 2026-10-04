---
title: Determining When an Item Is No Longer on the System Clipboard
nav: Determining When an Item I...
description: Toolkit.getDefaultToolkit().getSystemClipboard().setContents(ss, owner);
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20111105151115/http://java2s.com/Tutorial/Java/0120__Development/DeterminingWhenanItemIsNoLongerontheSystemClipboard.htm
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
