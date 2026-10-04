---
title: Java AWT BorderLayout add to top and bottom
nav: Java AWT BorderLayout add ...
description: privatestaticfinalString[] names = { "Red", "Green", "Blue", "Purple", "Greenish" };
section: Imported
order: 20056
source: http://www.java2s.com/ref/java/java-awt-borderlayout-add-to-top-and-bottom.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT BorderLayout add to top and bottom

```java title=Example.java
import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main extendsJFrame {
  privatestaticfinalString[] names = { "Red", "Green", "Blue", "Purple", "Greenish" };

  public Main() {

    setLayout(newBorderLayout(5, 5));

    JPanel center = newJPanel();
    JPanel bottom = newJPanel();

    add(newJComboBox(names), BorderLayout.NORTH);

    center.add(newJCheckBox("Background"));
    center.add(newJCheckBox("Foreground"));

    add(center, BorderLayout.CENTER);

    bottom.add(newJButton("Ok"));
    bottom.add(newJButton("Cancel"));

    add(bottom, BorderLayout.SOUTH);
  }/*fromwww.java2s.com*/publicstaticvoid main(String[] args) {
    Main gui = new Main();
    gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    gui.setSize(400, 125);
    gui.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java AWT BasicStroke create with line join and cap
- Java AWT BorderLayout add component
- Java AWT BorderLayout class
- Java AWT BorderLayout BorderLayout.LINE_END
- Java AWT BorderLayout BorderLayout.LINE_START
