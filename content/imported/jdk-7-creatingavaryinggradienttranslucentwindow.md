---
title: Creating a varying gradient translucent window
nav: Creating a varying gradien...
description: .isWindowTranslucencySupported(WindowTranslucency.PERPIXEL_TRANSLUCENT)) {
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20130223220141/http://www.java2s.com:80/Code/Java/JDK-7/Creatingavaryinggradienttranslucentwindow.htm
---
```java title=Example.java
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GraphicsDevice;
import java.awt.GraphicsDevice.WindowTranslucency;
import java.awt.GraphicsEnvironment;
import java.awt.Paint;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Test {
  public static void main(String[] args) {
    GraphicsEnvironment envmt = GraphicsEnvironment
        .getLocalGraphicsEnvironment();
    GraphicsDevice device = envmt.getDefaultScreenDevice();
    if (!device
        .isWindowTranslucencySupported(WindowTranslucency.PERPIXEL_TRANSLUCENT)) {
      System.out
          .println("Translucent windows are not supported on your system.");
      System.exit(0);
    }
    JFrame.setDefaultLookAndFeelDecorated(true);
    ApplicationWindow window = new ApplicationWindow();
    window.setVisible(true);
  }
}
class ApplicationWindow extends JFrame {
  public ApplicationWindow() {
    setBackground(new Color(0, 0, 0, 0));
    this.setSize(200, 200);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JPanel panel = new JPanel() {
      @Override
      protected void paintComponent(Graphics gradient) {
        if (gradient instanceof Graphics2D) {
          final int Red = 150;
          final int Green = 150;
          final int Blue = 150;
          Paint paint = new GradientPaint(0.0f, 0.0f, new Color(Red, Green,
              Blue, 0), getWidth(), getHeight(), new Color(Red, Green, Blue,
              255));
          Graphics2D gradient2d = (Graphics2D) gradient;
          gradient2d.setPaint(paint);
          gradient2d.fillRect(0, 0, getWidth(), getHeight());
        }
      }
    };
    this.setContentPane(panel);
  }
}
```

1.  Handling multiple file selection in the FileDialog class
---  ---
2.  Managing the Opacity of a Window
3.  Managing the Shape of a Window
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
