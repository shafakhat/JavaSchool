---
title: Java AWT Font get style
nav: Java AWT Font get style
description: Font f = g.getFont();/*fromwww.java2s.com*/String fontName = f.getName();
section: Imported
order: 20105
source: http://www.java2s.com/ref/java/java-awt-font-get-style.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Font get style

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

class DrawPanel extendsJPanel {

  publicvoid paint(Graphics g) {
    Font f = g.getFont();/*fromwww.java2s.com*/String fontName = f.getName();
    String fontFamily = f.getFamily();
    int fontSize = f.getSize();
    int fontStyle = f.getStyle();

    String msg = "Family: " + fontName;
    msg += ", Font: " + fontFamily;
    msg += ", Size: " + fontSize + ", Style: ";
    if ((fontStyle & Font.BOLD) == Font.BOLD)
      msg += "Bold ";
    if ((fontStyle & Font.ITALIC) == Font.ITALIC)
      msg += "Italic ";
    if ((fontStyle & Font.PLAIN) == Font.PLAIN)
      msg += "Plain ";

    g.drawString(msg, 4, 16);
  }
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    DrawPanel panel = new DrawPanel();

    JFrame application = newJFrame();

    application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    application.add(panel);
    application.setSize(250, 250);
    application.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java FocusTraversalPolicy get default focus component
- Java FocusTraversalPolicy get previous focusable component
- Java AWT Font class
- Java AWT Font available font families via GraphicsEnvironment class
- Java AWT Font create font and set to JButton
