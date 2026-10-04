---
title: Managing the Shape of a Window
nav: Managing the Shape of a Wi...
description: .isWindowTranslucencySupported(WindowTranslucency.PERPIXEL_TRANSLUCENT)) {
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20130223094558/http://www.java2s.com:80/Code/Java/JDK-7/ManagingtheShapeofaWindow.htm
---
Managing the Shape of a Window

```java title=Example.java
import java.awt.Color;
import java.awt.GraphicsDevice;
import java.awt.GraphicsDevice.WindowTranslucency;
import java.awt.GraphicsEnvironment;
import java.awt.Polygon;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;
import javax.swing.JButton;
import javax.swing.JFrame;
public class Test {
  public static void main(String[] args) {
    GraphicsEnvironment envmt = GraphicsEnvironment
        .getLocalGraphicsEnvironment();
    GraphicsDevice device = envmt.getDefaultScreenDevice();
    if (!device
        .isWindowTranslucencySupported(WindowTranslucency.PERPIXEL_TRANSLUCENT)) {
      System.out
          .println("Shaped windows are not supported on" + "your system.");
      System.exit(0);
    }
    ApplicationWindow window = new ApplicationWindow();
    window.setVisible(true);
  }
}
class ApplicationWindow extends JFrame {
  public ApplicationWindow() {
    this.setSize(300, 300);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.add(new JButton("asdf"));
    final Polygon myShape = getPolygon();
    this.addComponentListener(new ComponentAdapter() {
      @Override
      public void componentResized(ComponentEvent e) {
        setShape(myShape);
        ((JFrame) e.getSource()).setForeground(Color.red);
        ((JFrame) e.getSource()).setBackground(Color.red);
      }
    });
    this.setUndecorated(true);
  }
  private Polygon getPolygon() {
    int x1Points[] = { 0, 20, 100, 200, 330, 300, 200, 100 };
    int y1Points[] = { 100, 200, 310, 300, 200, 100, 10, 0 };
    Polygon polygon = new Polygon();
    for (int i = 0; i < y1Points.length; i++) {
      polygon.addPoint(x1Points[i], y1Points[i]);
    }
    return polygon;
  }
}
```

1.  Creating a varying gradient translucent window
---  ---
2.  Handling multiple file selection in the FileDialog class
3.  Managing the Opacity of a Window
4.  Managing Window types
5.  Mixing heavyweight and lightweight components
6.  New border types in Java 7:RaisedSoftBevelBorder
7.  New border types in Java 7:LineBorder width
8.  New border types in Java 7:LoweredSoftBevelBorder
9.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED)
10.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
11.  Using the new JLayer Decorator for a password field
12.  Managing extra mouse buttons and high resolution mouse wheels
13.  Using the NumericShaper.Range enumeration to support the display of digits
