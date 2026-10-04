---
title: Java AWT Graphics fill rectangle
nav: Java AWT Graphics fill rec...
description: // Demonstrate the key event handlers.import java.awt.Graphics;
section: Imported
order: 20128
source: http://www.java2s.com/ref/java/java-awt-graphics-fill-rectangle.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

To fill a rectangle using Java AWT Graphics.

```java title=Example.java

g.fillRect(10, 10, 60, 50);
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
    g.fillRect(10, 10, 60, 50);//fromwww.java2s.com
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

- Java AWT Graphics draw smiley face
- Java AWT Graphics draw with mouse
- Java AWT Graphics fill arc as rainbow
- Java AWT Graphics fill whole window
- Java AWT Graphics paint mode
