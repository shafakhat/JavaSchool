---
title: Java Swing Tutorial - Java Font.getTransform()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Font.getTransform() method.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/1460__Font.getTransform_.htm
---
```java title=Example.java
Back to Font  ↑
```

## Syntax

Font.getTransform() has the following syntax.

```java title=Example.java
public AffineTransform getTransform()
```

## Example

In the following code shows how to use Font.getTransform() method.

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
    System.out.println(f.getTransform());
    g.drawString("JavaSchool", 4, 16);
  }
}
```

- Back to Font ↑
