---
title: Java Swing Tutorial - Java Graphics.fillPolygon(Polygon p)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Graphics.fillPolygon(Polygon p) method.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0640__Graphics.fillPolygon_Polygon_p_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.fillPolygon(Polygon p) has the following syntax.

```java title=Example.java
publicvoid fillPolygon(Polygon p)
```

## Example

In the following code shows how to use Graphics.fillPolygon(Polygon p) method.

```java title=Example.java
import java.awt.Graphics;
import java.awt.Polygon;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    super.paintComponent(g);
    int radius = 40;
    int centerX = 50;
    int centerY = 100;
    Polygon p = new Polygon();
    centerX = 150;
    for (int i = 0; i < 5; i++)
        p.addPoint((int) (centerX + radius * Math.cos(i * 2 * Math.PI / 5)),
                (int) (centerY + radius * Math.sin(i * 2 * Math.PI / 5)));
    g.fillPolygon(p);
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
