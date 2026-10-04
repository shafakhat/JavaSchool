---
title: Java AWT Graphics2D draw String right alignment
nav: Java AWT Graphics2D draw S...
description: @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20139
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-string-right-alignment.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw String right alignment

```java title=Example.java
import java.awt.Color;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.font.FontRenderContext;
import java.awt.geom.Rectangle2D;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  Random rnd = newRandom();

  @Override//www.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    // antialising
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    // SanSerif
    g2d.setPaint(Color.BLUE);
    Font serif = newFont(Font.SERIF, Font.PLAIN, 30);
    g2d.setFont(serif);

    String sentence1 = "The quick brown fox jumped";
    String sentence2 = "over the lazy dog.";

    FontRenderContext fontRenderCtx = g2d.getFontRenderContext();
    Rectangle2D bounds1 = serif.getStringBounds(sentence1, fontRenderCtx);
    Rectangle2D bounds2 = serif.getStringBounds(sentence2, fontRenderCtx);

    int y = 50;
    int x = 0;
    FontMetrics fm = g2d.getFontMetrics();
    int spaceRow = fm.getDescent() + fm.getLeading() + fm.getAscent();

    x = (getParent().getWidth() - (int) bounds1.getWidth());
    g2d.drawString(sentence1, x, y);
    x = (getParent().getWidth() - (int) bounds2.getWidth());
    g2d.drawString(sentence2, x, y + spaceRow);
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

- Java AWT Graphics2D draw String
- Java AWT Graphics2D draw String center alignment
- Java AWT Graphics2D draw String left alignment
- Java AWT Graphics2D draw styled String
- Java AWT Graphics2D draw with mouse
