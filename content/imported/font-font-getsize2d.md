---
title: Java Swing Tutorial - Java Font.getSize2D()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Font.getSize2D() method.
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/1340__Font.getSize2D_.htm
---
```java title=Example.java
Back to Font  ↑
```

## Syntax

Font.getSize2D() has the following syntax.

```java title=Example.java
publicfloat getSize2D()
```

## Example

In the following code shows how to use Font.getSize2D() method.

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
    System.out.println(f.getSize2D());
    g.drawString("JavaSchool", 4, 16);
  }
}
```

- Back to Font ↑
