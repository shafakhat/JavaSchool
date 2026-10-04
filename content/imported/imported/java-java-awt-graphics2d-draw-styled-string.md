---
title: Java AWT Graphics2D draw styled String
nav: Java AWT Graphics2D draw s...
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20140
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-styled-string.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw styled String

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

    Font serif = newFont(Font.SERIF, Font.PLAIN, 50);
    attrStr.addAttribute(TextAttribute.FONT, serif, 0, 4);

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

- Java AWT Graphics2D draw String center alignment
- Java AWT Graphics2D draw String left alignment
- Java AWT Graphics2D draw String right alignment
- Java AWT Graphics2D draw with mouse
- Java AWT Graphics2D fill area
