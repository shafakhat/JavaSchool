---
title: Java AWT Color make color darker
nav: Java AWT Color make color ...
description: Imported from java2s.com: Java AWT Color make color darker
section: Imported
order: 20070
source: http://www.java2s.com/ref/java/java-awt-color-make-color-darker.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Description

Java AWT Color make color darker

```java title=Example.java
import java.awt.Color;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Color c = Color.WHITE;

    System.out.println(c);//www.java2s.com

    c = c.darker();
    System.out.println(c);

    System.out.println(Color.WHITE.darker());
  }
}
```

PreviousNext

## Related

- Java AWT Color class
- Java AWT Color create from hexadecimal integer value
- Java AWT Color create random color
- Java AWT Color predefined color constant value
- Java AWT Component check if has focus
