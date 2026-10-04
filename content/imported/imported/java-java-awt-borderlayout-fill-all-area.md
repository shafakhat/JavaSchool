---
title: Java AWT BorderLayout fill all area
nav: Java AWT BorderLayout fill...
description: //www.java2s.com/* Since the default layout manager for bordered containers is
section: Imported
order: 20058
source: http://www.java2s.com/ref/java/java-awt-borderlayout-fill-all-area.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT BorderLayout fill all area

```java title=Example.java
import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main {

  publicstaticvoid main(String[] args) {
    JFrame frame = newJFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setTitle("BorderLayout frame");
    //www.java2s.com/* Since the default layout manager for bordered containers is
     * already a BorderLayout, the following line is OPTIONAL here.
     */
    frame.getContentPane().setLayout(newBorderLayout());

    frame.getContentPane().add(newJButton("NORTH"),  BorderLayout.NORTH);
    // ... or BorderLayout.PAGE_START

    frame.getContentPane().add(newJButton("WEST"),   BorderLayout.WEST);
    // ... or BorderLayout.LINE_START

    frame.getContentPane().add(newJButton("EAST"),   BorderLayout.EAST);
    // ... or BorderLayout.LINE_END

    frame.getContentPane().add(newJButton("SOUTH"),  BorderLayout.SOUTH);
    // ... or BorderLayout.PAGE_END

    frame.getContentPane().add(newJButton("CENTER"), BorderLayout.CENTER);
    frame.pack();
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT BorderLayout add to top and bottom
- Java AWT BorderLayout BorderLayout.LINE_END
- Java AWT BorderLayout BorderLayout.LINE_START
- Java AWT CardLayout class
- Java AWT CardLayout move to next component
