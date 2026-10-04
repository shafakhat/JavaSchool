---
title: Java Swing Tutorial - Java Graphics.create()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Graphics.create() method.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0120__Graphics.create_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.create() has the following syntax.

```java title=Example.java
publicabstract Graphics create()
```

## Example

In the following code shows how to use Graphics.create() method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.setColor (Color.red);
    Graphics clippedGraphics = g.create();
    clippedGraphics.drawRect (0,0,100,100);
    clippedGraphics.clipRect (25, 25, 50, 50);
    clippedGraphics.drawLine (0,0,100,100);
    clippedGraphics.dispose();
    clippedGraphics=null;
    g.drawLine (0,100,100,0);
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

- Back to Graphics ↑
