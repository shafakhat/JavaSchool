---
title: Java AWT Dimension class
nav: Java AWT Dimension class
description: An object of the Dimension class is used to represent the size of a component.
section: Imported
order: 20074
source: http://www.java2s.com/ref/java/java-awt-dimension-class.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

Dimension class wraps the width and height of a component.

An object of the Dimension class is used to represent the size of a component.

```java title=Example.java
// Dimension with a width and height of 200 and 20 Dimension d  = newDimension(200, 20);

// Set the size of closeButton to 200 X 20. //Both of the statements have the same effect.
closeButton.setSize(200, 20); /*fromwww.java2s.com*/
closeButton.setsize(d);

// Get the size of closeButton Dimension d2 = closeButton.getSize();
int width = d2.width;
int height = d2.height;
```

```java title=Example.java
import java.awt.Dimension;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Dimension d  = newDimension(200, 20);
    //fromwww.java2s.comSystem.out.println(d);
  }
}
```

PreviousNext

## Related

- Java AWT Component grab focus in window
- Java AWT Component get root focus cycle ancestor
- Java AWT Container get FocusTraversalPolicy
- Java AWT EventQueue run Swing application
- Java AWT FileDialog handle multiple file selection
