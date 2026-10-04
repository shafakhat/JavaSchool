---
title: Java Tutorial - Java CardLayout.previous(Container parent)
nav: Java Tutorial - Java CardL...
description: CardLayout.previous(Container parent) has the following syntax.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/Java_CardLayout_previous_Container_parent_.htm
---
Next »CardLayout (3268/9945)« Previous

### Syntax

CardLayout.previous(Container parent) has the following syntax.

```java title=Example.java
publicvoid previous(Container parent)
```

### Example

In the following code shows how to use CardLayout.previous(Container parent) method.

```java title=Example.java
/*fromwww.java2s.com*/import java.awt.CardLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main {

  publicstaticvoid main(String[] args) {
    JFrame aWindow = new JFrame();
    aWindow.setSize(400, 400);
    aWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    aWindow.add(new CardLayoutPanel());
    aWindow.setVisible(true);
  }
}

class CardLayoutPanel extends JPanel implements ActionListener {
  CardLayout card = new CardLayout(50, 50);

  public CardLayoutPanel() {
    setLayout(card);
    JButton button;
    for (int i = 1; i <= 6; i++) {
      add(button = new JButton("Press " + i), "Card" + i);
      button.addActionListener(this);
    }
    card.previous(this);
  }
  publicvoid actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt »

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
