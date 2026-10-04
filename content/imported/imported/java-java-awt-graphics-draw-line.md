---
title: Java AWT Graphics draw line
nav: Java AWT Graphics draw line
description: // Demonstrate the key event handlers.import java.awt.Graphics;
section: Imported
order: 20121
source: http://www.java2s.com/ref/java/java-awt-graphics-draw-line.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

To draw line using Java AWT Graphics

```java title=Example.java

g.drawLine(0, 0, 100, 90);
```

Full source

```java title=Example.java
// Demonstrate the key event handlers.import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;

class SimpleKey extendsJLabel {

  publicvoid paint(Graphics g) {
    // Draw lines.
    g.drawLine(0, 0, 100, 90); //www.java2s.com
  }
}

publicclass Main {
  publicstaticvoid main(String args[]) {
    // Create the frame on the event dispatching thread.SwingUtilities.invokeLater(newRunnable() {
      publicvoid run() {
        // Create a new JFrame container.JFrame jfrm = newJFrame("java2s.com");

        // Give the frame an initial size.
        jfrm.setSize(220, 200);

        // Terminate the program when the user closes the application.
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Add the label to the content pane.
        jfrm.add(new SimpleKey());

        // Display the frame.
        jfrm.setVisible(true);

      }
    });
  }
}
```

PreviousNext

## Related

- Java AWT GradientPaint create
- Java AWT Graphics double buffer
- Java AWT Graphics draw arc
- Java AWT Graphics draw lines with random location
- Java AWT Graphics draw oval
