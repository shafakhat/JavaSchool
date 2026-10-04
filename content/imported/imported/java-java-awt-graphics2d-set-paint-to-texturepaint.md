---
title: Java AWT Graphics2D set paint to TexturePaint
nav: Java AWT Graphics2D set pa...
description: @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
section: Imported
order: 20152
source: http://www.java2s.com/ref/java/java-awt-graphics2d-set-paint-to-texturepaint.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D set paint to TexturePaint

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.TexturePaint;
import java.awt.geom.RoundRectangle2D;
import java.awt.image.BufferedImage;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanel {
  @Override//fromwww.java2s.compublicvoid paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2d = (Graphics2D) g; // cast g to Graphics2D// draw 2D rounded rectangle with a buffered backgroundBufferedImage buffImage = newBufferedImage(10, 10, BufferedImage.TYPE_INT_RGB);

    // obtain Graphics2D from buffImage and draw on itGraphics2D gg = buffImage.createGraphics();
    gg.setColor(Color.YELLOW);
    gg.fillRect(0, 0, 10, 10);
    gg.setColor(Color.BLACK);
    gg.drawRect(1, 1, 6, 6);

    // paint buffImage onto the JFrame
    g2d.setPaint(newTexturePaint(buffImage, newRectangle(10, 10)));
    g2d.fill(new RoundRectangle2D.Double(155, 30, 75, 100, 50, 50));
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = newJFrame("Drawing 2D shapes");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Main Main = new Main();
    frame.add(Main);
    frame.setSize(425, 200);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT Graphics2D set gradient paint
- Java AWT Graphics2D set linear gradient paint
- Java AWT Graphics2D set paint to red color
- Java AWT Graphics2D set radial gradient paint
- Java AWT Graphics2D set stroke to BasicStroke
