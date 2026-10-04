---
title: Java AWT AttributedString set background color
nav: Java AWT AttributedString ...
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20051
source: http://www.java2s.com/ref/java/java-awt-attributedstring-set-background-color.html
---
- java.text
- java.text AttributedString DateFormat DateFormatSymbols DecimalFormat DecimalFormatSymbols Format NumberFormat SimpleDateFormat

## Description

Java AWT AttributedString set background color

```java title=Example.java
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Paint;
import java.awt.RenderingHints;
import java.awt.font.TextAttribute;
import java.text.AttributedString;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();

  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    AttributedString attrStr = newAttributedString("www.demo2s.com");

    attrStr.addAttribute(TextAttribute.BACKGROUND, Color.BLUE, 0, 4);

    g2d.drawString(attrStr.getIterator(), 50, 100);
  }

  publicstaticvoid main(String[] args) {
    // create frame for MainJFrame frame = newJFrame("java2s.com");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    Main Main = new Main();
    frame.add(Main);
    frame.setSize(300, 210);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java SQL Timestamp create from LocalDateTime
- Java SQL Timestamp format to String like "1969-12-31 19:25:12"
- Java AWT AttributedString create
- Java AWT AttributedString set font
- Java AWT AttributedString set strike through
