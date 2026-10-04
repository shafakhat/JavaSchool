---
title: Java Swing Tutorial - Java FontMetrics.getDescent()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FontMetrics.getDescent() method.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FontMetrics/0180__FontMetrics.getDescent_.htm
---
## Syntax

FontMetrics.getDescent() has the following syntax.

```java title=Example.java
public int getDescent()
```

## Example

In the following code shows how to use FontMetrics.getDescent() method.

```java title=Example.java
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public Main() {
    setFont(new Font("TimesRoman", Font.BOLD | Font.ITALIC, 48));
    setSize(225, 175);
  }
  public void paint(Graphics g) {
    g.translate(100, 100);
    FontMetrics fm = null;
    int ascent, descent, leading, width1, width2, height;
    String string1 = "JavaSchool";
    String string2 = "JavaSchool";
    int xPos = 25, yPos = 50;
    fm = g.getFontMetrics();
    ascent = fm.getAscent();
    descent = fm.getDescent();
    leading = fm.getLeading();
    height = fm.getHeight();
    width1 = fm.stringWidth(string1);
    width2 = fm.stringWidth(string2);
    g.drawString(string1, xPos, yPos);
    g.drawLine(xPos, yPos - ascent - leading, xPos + width1, yPos - ascent
        - leading);
    g.drawLine(xPos, yPos - ascent, xPos + width1, yPos - ascent);
    g.drawLine(xPos, yPos, xPos + width1, yPos);
    g.drawLine(xPos, yPos + descent, xPos + width1, yPos + descent);
    g.drawString(string2, xPos, yPos + height);
    g.drawLine(xPos, yPos - ascent - leading + height, xPos + width2, yPos
        - ascent - leading + height);
    g.drawLine(xPos, yPos - ascent + height, xPos + width2, yPos - ascent
        + height);
    g.drawLine(xPos, yPos + height, xPos + width2, yPos + height);
    g.drawLine(xPos, yPos + descent + height, xPos + width2, yPos + descent
        + height);
  }
  public static void main(String[] args) {
    JFrame f = new JFrame();
    f.add(new Main());
    f.setSize(300, 300);
    f.setVisible(true);
  }
}
```
