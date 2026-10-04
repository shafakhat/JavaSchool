---
title: Java Swing Tutorial - Java Font.getSize()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Font.getSize() method.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/1320__Font.getSize_.htm
---
```java title=Example.java
Back to Font  ↑
```

## Syntax

Font.getSize() has the following syntax.

```java title=Example.java
publicint getSize()
```

## Example

In the following code shows how to use Font.getSize() method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
publicclass Main extends JFrame {
  publicstaticvoid main(String[] a) {
    Main f = new Main();
    f.setSize(300, 300);
    f.setVisible(true);
  }
  publicvoid paint(Graphics g) {
    Font f = g.getFont();
    int fontSize = f.getSize();
    int fontStyle = f.getStyle();
    String msg = ", Size: " + fontSize + ", Style: ";
    if ((fontStyle & Font.BOLD) == Font.BOLD)
      msg += "Bold ";
    if ((fontStyle & Font.ITALIC) == Font.ITALIC)
      msg += "Italic ";
    if ((fontStyle & Font.PLAIN) == Font.PLAIN)
      msg += "Plain ";
    g.drawString(msg, 4, 16);
  }
}
```

- Back to Font ↑
