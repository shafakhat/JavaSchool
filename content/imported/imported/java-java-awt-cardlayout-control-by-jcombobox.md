---
title: Java AWT CardLayout control by JComboBox
nav: Java AWT CardLayout contro...
description: frame.getContentPane().add(comboBoxPanel, BorderLayout.PAGE_START);
section: Imported
order: 20064
source: http://www.java2s.com/ref/java/java-awt-cardlayout-control-by-jcombobox.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT CardLayout control by JComboBox

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main {
   publicstaticvoid main(String[] args) {
      JFrame frame = newJFrame();
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setTitle("CardLayout frame");
      /*fromwww.java2s.com*/JPanel cardPanel = newJPanel();
      cardPanel.setLayout(newCardLayout());
      cardPanel.setPreferredSize(newDimension(300, 400));

      JPanel bluePanel = newJPanel();
      JPanel redPanel = newJPanel();
      bluePanel.setBackground(Color.blue);
      redPanel.setBackground(Color.red);

      cardPanel.add(bluePanel, "BLUE PANEL");
      cardPanel.add(redPanel, "RED PANEL");

      JPanel comboBoxPanel = newJPanel();
      String comboBoxItems[] = { "BLUE PANEL", "RED PANEL" };
      JComboBox<String> cb = newJComboBox<>(comboBoxItems);
      cb.setEditable(false);
      cb.addItemListener(newItemListener(){
         @Overridepublicvoid itemStateChanged(ItemEvent evt) {
            CardLayout cl = (CardLayout)(cardPanel.getLayout());
            cl.show(cardPanel, (String)evt.getItem());
         }
      });
      comboBoxPanel.add(cb);

      frame.getContentPane().add(comboBoxPanel, BorderLayout.PAGE_START);
      frame.getContentPane().add(cardPanel, BorderLayout.CENTER);

      frame.pack();
      frame.setVisible(true);
   }
}
```

PreviousNext

## Related

- Java AWT BorderLayout fill all area
- Java AWT CardLayout class
- Java AWT CardLayout move to next component
- Java AWT Color class
- Java AWT Color create from hexadecimal integer value
