---
title: Java AWT Graphics2D draw with mouse
nav: Java AWT Graphics2D draw w...
description: publicclass Main extendsJPanelimplementsMouseListener, MouseMotionListener {
section: Imported
order: 20146
source: http://www.java2s.com/ref/java/java-awt-graphics2d-draw-with-mouse.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Graphics2D draw with mouse

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.geom.GeneralPath;
import java.awt.geom.Path2D;
import java.awt.geom.Point2D;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJPanelimplementsMouseListener, MouseMotionListener {

  Path2D oneDrawing = newPath2D.Double();
  List<Path2D> drawings = newArrayList<>();
  privatePoint2D anchorPt;

  @Override//www.java2s.comprotectedvoid paintComponent(Graphics g) {
    super.paintComponent(g);

    Graphics2D g2d = (Graphics2D) g;
    g2d.setBackground(Color.WHITE);
    g2d.clearRect(0, 0, getParent().getWidth(), getParent().getHeight());
    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

    g2d.setPaint(Color.BLACK);
    if (oneDrawing != null) {
      g2d.draw(oneDrawing);
    }
    for (Path2D gp : drawings) {
      g2d.draw(gp);
    }

  }

  @Overridepublicvoid mouseClicked(MouseEvent e) {
  }

  @Overridepublicvoid mousePressed(MouseEvent e) {
    anchorPt = (Point2D) e.getPoint().clone();
    oneDrawing = newGeneralPath();
    oneDrawing.moveTo(anchorPt.getX(), anchorPt.getY());
    repaint();
  }

  @Overridepublicvoid mouseReleased(finalMouseEvent e) {
    if (anchorPt != null) {
      drawings.add(oneDrawing);
      oneDrawing = null;
    }
    repaint();
  }

  @Overridepublicvoid mouseEntered(MouseEvent e) {
  }

  @Overridepublicvoid mouseExited(MouseEvent e) {
  }

  @Overridepublicvoid mouseDragged(MouseEvent e) {
    oneDrawing.lineTo(e.getX(), e.getY());
    repaint();
  }

  @Overridepublicvoid mouseMoved(MouseEvent e) {
  }

  publicstaticvoid main(String[] args) {
    final Main c = new Main();
    c.addMouseListener(c);
    c.addMouseMotionListener(c);
    c.setPreferredSize(newDimension(409, 726));
    JFrame frame = newJFrame("java2s.com");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    frame.add(c);
    frame.setSize(300, 250);
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT Graphics2D draw String left alignment
- Java AWT Graphics2D draw String right alignment
- Java AWT Graphics2D draw styled String
- Java AWT Graphics2D fill area
- Java AWT Graphics2D fill rectangle with Rectangle2D
