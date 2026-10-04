---
title: Managing the Opacity of a Window
nav: Managing the Opacity of a ...
description: GraphicsEnvironment graphicsEnvironment = GraphicsEnvironment
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20130223220146/http://www.java2s.com:80/Code/Java/JDK-7/ManagingtheOpacityofaWindow.htm
---
Managing the Opacity of a Window

```java title=Example.java
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;
public class Test {
  public static void main(String[] args) {
    JFrame.setDefaultLookAndFeelDecorated(true);
    GraphicsEnvironment graphicsEnvironment = GraphicsEnvironment
        .getLocalGraphicsEnvironment();
    GraphicsDevice graphicsDevice = graphicsEnvironment
        .getDefaultScreenDevice();
    if (!graphicsDevice
        .isWindowTranslucencySupported(GraphicsDevice.WindowTranslucency.TRANSLUCENT)) {
      System.err.println("Translucency is not supported on this platform");
      System.exit(0);
    }
    ApplicationWindow window = new ApplicationWindow();
    window.setOpacity(0.75f);
    window.setVisible(true);
  }
}
class ApplicationWindow extends JFrame {
  public ApplicationWindow() {
    this.setBounds(100, 100, 200, 200);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setType(Type.NORMAL);
    JButton exitButton = new JButton("Exit");
    this.add(exitButton);
    exitButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        System.exit(0);
      }
    });
  }
}
```

1.  Creating a varying gradient translucent window
---  ---
2.  Handling multiple file selection in the FileDialog class
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
