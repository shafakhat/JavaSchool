---
title: Java Tutorial - Java EventQueue.peekEvent()
nav: Java Tutorial - Java Event...
description: In the following code shows how to use EventQueue.peekEvent() method.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/EventQueue/Java_EventQueue_peekEvent_.htm
---
### Syntax

EventQueue.peekEvent() has the following syntax.

```java title=Example.java
public AWTEvent peekEvent()
```

### Example

In the following code shows how to use EventQueue.peekEvent() method.

```java title=Example.java
import java.awt.AWTEvent;
import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel implements ActionListener {
  Main() {
    JButton button = new JButton("Click to chooose the first point");
    add(button);
    button.addActionListener(this);
  }
  public void actionPerformed(ActionEvent evt) {
    Graphics g = getGraphics();
    Point p = getClick();
    g.drawOval(p.x - 2, p.y - 2, 4, 4);
    Point q = getClick();
    g.drawOval(q.x - 2, q.y - 2, 4, 4);
    g.drawLine(p.x, p.y, q.x, q.y);
    g.dispose();
  }
  public Point getClick() {
    EventQueue eq = Toolkit.getDefaultToolkit().getSystemEventQueue();
    while (true) {
      try {
        AWTEvent pEvent = eq.peekEvent();
        AWTEvent evt = eq.getNextEvent();
        if (evt.getID() == MouseEvent.MOUSE_PRESSED) {
          MouseEvent mevt = (MouseEvent) evt;
          Point p = mevt.getPoint();
          Point top = getRootPane().getLocation();
          p.x -= top.x;
          p.y -= top.y;
          return p;
        }
      } catch (InterruptedException e) {
      }
    }
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.setSize(300, 200);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.add(new Main());
    frame.setVisible(true);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
