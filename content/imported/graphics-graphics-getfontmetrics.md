---
title: Java Swing Tutorial - Java Graphics.getFontMetrics()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Graphics.getFontMetrics() method.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0840__Graphics.getFontMetrics_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.getFontMetrics() has the following syntax.

```java title=Example.java
public FontMetrics getFontMetrics()
```

## Example

In the following code shows how to use Graphics.getFontMetrics() method.

```java title=Example.java
import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    int fontSize = 20;
    g.setFont(new Font("TimesRoman", Font.PLAIN, fontSize));
    FontMetrics fm = g.getFontMetrics();
    String s = "JavaSchool";
    int stringWidth = fm.stringWidth(s);
    int w = 200;
    int h = 200;
    int x = (w - stringWidth) / 2;
    int baseline = fm.getMaxAscent() +
                       (h - (fm.getAscent() + fm.getMaxDecent()))/2;
    int ascent  = fm.getMaxAscent();
    int descent = fm.getMaxDecent();
    int fontHeight = fm.getMaxAscent() + fm.getMaxDecent();
    g.setColor(Color.white);
    g.fillRect(x, baseline-ascent , stringWidth, fontHeight);
    g.setColor(Color.gray);
    g.drawLine(x, baseline, x+stringWidth, baseline);
    g.setColor(Color.red);
    g.drawLine(x, baseline+descent, x+stringWidth, baseline+descent);
    g.setColor(Color.blue);
    g.drawLine(x, baseline-ascent,
               x+stringWidth, baseline-ascent);
    g.setColor(Color.black);
    g.drawString(s, x, baseline);
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
