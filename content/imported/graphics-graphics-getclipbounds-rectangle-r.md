---
title: Java Swing Tutorial - Java Graphics .getClipBounds (Rectangle r)
nav: Java Swing Tutorial - Java...
description: Graphics.getClipBounds(Rectangle r) has the following syntax.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0760__Graphics.getClipBounds_Rectangle_r_.htm
---
## Syntax

Graphics.getClipBounds(Rectangle r) has the following syntax.

```java title=Example.java
public Rectangle getClipBounds(Rectangle r)
```

## Example

In the following code shows how to use Graphics.getClipBounds(Rectangle r) method.

```java title=Example.java
import java.awt.Graphics;
import java.awt.Rectangle;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    super.paint(g);
    Rectangle r = g.getClipBounds();
    g.drawLine(0,0,r.width, r.height);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```
