---
title: Java Tutorial - Java CardLayout(int hgap, int vgap) Constructor
nav: Java Tutorial - Java CardL...
description: CardLayout(int hgap, int vgap) constructor from CardLayout has the following syntax.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/CardLayout/Java_CardLayout_int_hgap_int_vgap_Constructor.htm
---
Next »CardLayout (3254/9945)« Previous

### Syntax

CardLayout(int hgap, int vgap) constructor from CardLayout has the following syntax.

```java title=Example.java
public CardLayout(int hgap,   int vgap)
```

### Example

In the following code shows how to use CardLayout.CardLayout(int hgap, int vgap) constructor.

```java title=Example.java
import java.awt.CardLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/*fromwww.java2s.com*/import javax.swing.JButton;
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
  }
  publicvoid actionPerformed(ActionEvent e) {
    card.next(this);
  }
}
```

Next »« PreviousHome » Java Tutorial » java.awt »

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
