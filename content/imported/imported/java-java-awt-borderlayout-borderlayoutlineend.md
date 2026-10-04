---
title: Java AWT BorderLayout BorderLayout.LINE_END
nav: Java AWT BorderLayout Bord...
description: frame.getContentPane().add(bluePanel, BorderLayout.LINE_START);
section: Imported
order: 20057
source: http://www.java2s.com/ref/java/java-awt-borderlayout-borderlayoutlineend.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT BorderLayout BorderLayout.LINE_END

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

publicclass Main {
   publicstaticvoid main(String[] args) {
      JFrame frame = newJFrame();
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setTitle("My First Frame");
      //fromwww.java2s.comJPanel bluePanel = newJPanel();
      JPanel redPanel = newJPanel();

      JLabel label = newJLabel("<-- pick your side -->");

      frame.getContentPane().add(label, BorderLayout.CENTER);

      bluePanel.setBackground(Color.blue);
      redPanel.setBackground(Color.red);

      frame.getContentPane().add(bluePanel, BorderLayout.LINE_START);
      frame.getContentPane().add(redPanel, BorderLayout.LINE_END);

      JButton blueButton = newJButton("PICK BLUE TEAM");
      JButton redButton = newJButton("PICK RED TEAM");

      bluePanel.add(blueButton);
      redPanel.add(redButton);

      frame.pack();
      frame.setVisible(true);
   }
}
```

PreviousNext

## Related

- Java AWT BorderLayout add component
- Java AWT BorderLayout class
- Java AWT BorderLayout add to top and bottom
- Java AWT BorderLayout BorderLayout.LINE_START
- Java AWT BorderLayout fill all area
