---
title: Java Swing Tutorial - Java BasicStroke CAP_SQUARE
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.CAP_SQUARE field.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0080__BasicStroke.CAP_SQUARE.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Syntax

BasicStroke.CAP_SQUARE has the following syntax.

```java title=Example.java
publicstaticfinalint CAP_SQUARE
```

## Example

In the following code shows how to use BasicStroke.CAP_SQUARE field.

```java title=Example.java
import java.awt.BasicStroke;
import java.awt.Graphics;
import java.awt.Graphics2D;
//fromwww.java2s.comimport javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extends JPanel {

  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;

    BasicStroke bs = new BasicStroke(16.0f, BasicStroke.CAP_SQUARE, BasicStroke.JOIN_BEVEL);
    g2.setStroke(bs);
    g.drawLine(30, 20, 270, 20);
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

- Back to BasicStroke ↑
