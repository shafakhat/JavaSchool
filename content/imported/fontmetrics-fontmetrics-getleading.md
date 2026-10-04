---
title: Java Swing Tutorial - Java FontMetrics.getLeading()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FontMetrics.getLeading() method.
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FontMetrics/0260__FontMetrics.getLeading_.htm
---
```java title=Example.java
Back to FontMetrics  ↑
```

## Syntax

FontMetrics.getLeading() has the following syntax.

```java title=Example.java
publicint getLeading()
```

## Example

In the following code shows how to use FontMetrics.getLeading() method.

```java title=Example.java
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import javax.swing.JFrame;
publicclass Main extends JFrame {
  public Main() {
    super("Demonstrating FontMetrics");
    setSize(510, 210);
    setVisible(true);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  }
  publicvoid paint(Graphics g) {
    g.setFont(new Font("SansSerif", Font.BOLD, 12));
    FontMetrics fm = g.getFontMetrics();
    g.drawString("Current font: " + g.getFont(), 10, 40);
    g.drawString("Ascent: " + fm.getAscent(), 10, 55);
    g.drawString("Descent: " + fm.getDescent(), 10, 70);
    g.drawString("Height: " + fm.getHeight(), 10, 85);
    g.drawString("Leading: " + fm.getLeading(), 10, 100);
    Font font = new Font("Serif", Font.ITALIC, 14);
    fm = g.getFontMetrics(font);
    g.setFont(font);
    g.drawString("Current font: " + font, 10, 130);
    g.drawString("Ascent: " + fm.getAscent(), 10, 145);
    g.drawString("Descent: " + fm.getDescent(), 10, 160);
    g.drawString("Height: " + fm.getHeight(), 10, 175);
    g.drawString("Leading: " + fm.getLeading(), 10, 190);
  }
  publicstaticvoid main(String args[]) {
    Main app = new Main();
  }
}
```

- Back to FontMetrics ↑
