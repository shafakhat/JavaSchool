---
title: Java AWT Color create from hexadecimal integer value
nav: Java AWT Color create from...
description: Imported from java2s.com: Java AWT Color create from hexadecimal integer value
section: Imported
order: 20067
source: http://www.java2s.com/ref/java/java-awt-color-create-from-hexadecimal-integer-value.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Color create from hexadecimal integer value

```java title=Example.java
import java.awt.Color;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main extendsJFrame {
  public Main() {
    super("JButton");

    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setLayout(newFlowLayout());

    JButton bn = newJButton("Close");

    bn.setForeground(newColor(0xffffdd));
    //fromwww.java2s.com
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

- Java AWT CardLayout move to next component
- Java AWT CardLayout control by JComboBox
- Java AWT Color class
- Java AWT Color create random color
- Java AWT Color make color darker
