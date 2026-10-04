---
title: Java AWT Font create font and set to JButton
nav: Java AWT Font create font ...
description: Imported from java2s.com: Java AWT Font create font and set to JButton
section: Imported
order: 20098
source: http://www.java2s.com/ref/java/java-awt-font-create-font-and-set-to-jbutton.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Font create font and set to JButton

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.Font;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main extendsJFrame {
  public Main() {
    super("JButton");

    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setLayout(newFlowLayout());

    //fromwww.java2s.comJButton bn = newJButton("Close");
    Font font = newFont("Arial", Font.BOLD, 15);
    bn.setFont(font);

    getContentPane().add(bn);
  }

  publicstaticvoid main(String[] args) {
    Main frame = new Main();
    frame.pack();
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT Font class
- Java AWT Font get style
- Java AWT Font available font families via GraphicsEnvironment class
- Java AWT Font derive font from swing component
- Java AWT FontMetrics from Graphics
