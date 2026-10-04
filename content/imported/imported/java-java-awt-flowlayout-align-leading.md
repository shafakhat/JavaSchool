---
title: Java AWT FlowLayout align leading
nav: Java AWT FlowLayout align ...
description: FlowLayout.LEADING is depending on the orientation of the container.
section: Imported
order: 20092
source: http://www.java2s.com/ref/java/java-awt-flowlayout-align-leading.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

FlowLayout.LEADING is depending on the orientation of the container.

```java title=Example.java
import java.awt.ComponentOrientation;
import java.awt.Container;
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main {
    publicstaticvoid main(String[] args) {
        int horizontalGap = 20;
        int verticalGap = 10;
        JFrame frame = newJFrame("Flow Layout Test");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container contentPane = frame.getContentPane();
        FlowLayout flowLayout = newFlowLayout(FlowLayout.LEADING, horizontalGap, verticalGap);
        contentPane.setLayout(flowLayout);
        frame.applyComponentOrientation(ComponentOrientation.RIGHT_TO_LEFT);

        for (int i = 1; i <= 3; i++) {
            contentPane.add(newJButton("Button " + i));
        }/*fromwww.java2s.com*/

        frame.pack();
        frame.setVisible(true);
    }
}
```

PreviousNext

## Related

- Java AWT FileDialog create
- Java AWT FlowLayout set alignment
- Java AWT FlowLayout class
- Java AWT FlowLayout align right
- Java AWT FlowLayout layout components in one row
