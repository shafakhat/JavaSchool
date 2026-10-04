---
title: Java AWT FlowLayout class
nav: Java AWT FlowLayout class
description: // Repaint when status of a check box changes.publicvoid itemStateChanged(ItemEvent ie) {
section: Imported
order: 20091
source: http://www.java2s.com/ref/java/java-awt-flowlayout-class.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

FlowLayout is the default layout manager.

Here are the constructors for FlowLayout:

```java title=Example.java
FlowLayout()
FlowLayout(int how)
FlowLayout(int how, int horz, int vert)
```

Valid values for how are as follows:

```java title=Example.java
FlowLayout.LEFT
FlowLayout.CENTER
FlowLayout.RIGHT
FlowLayout.LEADING
FlowLayout.TRAILING
```

```java title=Example.java
import java.awt.Container;
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main {
    publicstaticvoid main(String[] args) {
        JFrame frame = newJFrame("Flow Layout Test");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container contentPane = frame.getContentPane();
        contentPane.setLayout(newFlowLayout());

        for (int i = 1; i <= 3; i++) {
            contentPane.add(newJButton("Button " + i));
        }/*fromwww.java2s.com*/

        frame.pack();
        frame.setVisible(true);
    }
}
```

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JPanel;

class FlowLayoutDemo extendsJPanelimplementsItemListener {

  String msg = "";
  JCheckBox windows, android, solaris, mac;

  publicvoid init() {
    // set left-aligned flow layout
    setLayout(newFlowLayout(FlowLayout.LEFT));

    windows = newJCheckBox("Windows", null, true);
    android = newJCheckBox("Android");
    solaris = newJCheckBox("Solaris");
    mac = newJCheckBox("Mac OS");

    add(windows);//fromwww.java2s.com
    add(android);
    add(solaris);
    add(mac);

    // register to receive item events
    windows.addItemListener(this);
    android.addItemListener(this);
    solaris.addItemListener(this);
    mac.addItemListener(this);
  }

  // Repaint when status of a check box changes.publicvoid itemStateChanged(ItemEvent ie) {
    String msg = "Current state: ";
    msg = "  Windows: " + windows.isSelected();

    msg = "  Android: " + android.isSelected();

    msg = "  Solaris: " + solaris.isSelected();

    msg = "  Mac: " + mac.isSelected();
    System.out.println(msg);
  }

}

publicclass Main {
  publicstaticvoid main(String[] args) {
    FlowLayoutDemo panel = new FlowLayoutDemo();

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

- Java AWT FileDialog handle multiple file selection
- Java AWT FileDialog create
- Java AWT FlowLayout set alignment
- Java AWT FlowLayout align leading
- Java AWT FlowLayout align right
