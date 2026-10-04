---
title: Java AWT BorderLayout class
nav: Java AWT BorderLayout class
description: The BorderLayout class implements a common layout style for top-level windows.
section: Imported
order: 20059
source: http://www.java2s.com/ref/java/java-awt-borderlayout-class.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

The BorderLayout class implements a common layout style for top-level windows.

The BorderLayout has four narrow, fixed-width components at the four edges of a rectangle and one large area in the center.

The four sides are referred to as north, south, east, and west.

The middle area is called the center.

Here are the constructors defined by BorderLayout:

```java title=Example.java
BorderLayout()
BorderLayout(int horz, int vert)
```

BorderLayout defines the following constants that specify the regions:

```java title=Example.java
BorderLayout.CENTER
BorderLayout.SOUTH
BorderLayout.EAST
BorderLayout.WEST
BorderLayout.NORTH
```

When adding components, you will use these constants with the following form of add(), which is defined by Container:

```java title=Example.java
void add(Component  compRef, Object region)
```

Here is an example of a BorderLayout with a component in each layout area:

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JFrame;
import java.awt.Container;
import javax.swing.JButton;

publicclass Main {
    publicstaticvoid main(String[] args) {
        JFrame frame = newJFrame("BorderLayout Test");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container container = frame.getContentPane();

        // Add a button to each of the five areas of the BorderLayout
        container.add(newJButton("North"), BorderLayout.NORTH);
        container.add(newJButton("South"), BorderLayout.SOUTH);
        container.add(newJButton("East"), BorderLayout.EAST);
        container.add(newJButton("West"), BorderLayout.WEST);
        container.add(newJButton("Center"), BorderLayout.CENTER);

        frame.pack();/*fromwww.java2s.com*/
        frame.setVisible(true);
    }
}
```

```java title=Example.java
import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;

class Demo extendsJPanel {
  public Demo() {
    setLayout(newBorderLayout());
    add(newJButton("This is across the top."), BorderLayout.NORTH);
    add(newJLabel("The footer message might go here."), BorderLayout.SOUTH);
    add(newJButton("Right"), BorderLayout.EAST);
    add(newJButton("Left"), BorderLayout.WEST);

    add(newJTextArea("demo from demo2s.com"), BorderLayout.CENTER);
  }/*www.java2s.com*/
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    Demo panel = new Demo();

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

- Java AWT BasicStroke create dashed line
- Java AWT BasicStroke create with line join and cap
- Java AWT BorderLayout add component
- Java AWT BorderLayout add to top and bottom
- Java AWT BorderLayout BorderLayout.LINE_END
