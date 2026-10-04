---
title: Mixing heavyweight and lightweight components
nav: Mixing heavyweight and lig...
description: 10. BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/20130223214959/http://www.java2s.com:80/Code/Java/JDK-7/Mixingheavyweightandlightweightcomponents.htm
---
```java title=Example.java
import javax.swing.SwingUtilities;
import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
public class Test {
  public static void main(String[] args) {
    ApplicationWindow window = new ApplicationWindow();
    window.setVisible(true);
  }
}
class ApplicationWindow extends JFrame {
  public ApplicationWindow() {
    this.setSize(200, 100);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setLayout(new FlowLayout());
    Button exitButton = new Button("Exit");
    exitButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        System.exit(0);
      }
    });
    this.add(exitButton);
    JMenuBar menuBar = new JMenuBar();
    JMenu menu = new JMenu("Overlapping Menu");
    JMenuItem menuItem = new JMenuItem("Overlapping Item");
    menu.add(menuItem);
    menuBar.add(menu);
    this.setJMenuBar(menuBar);
    this.validate();
  }
}
```

1.  Creating a varying gradient translucent window
---  ---
2.  Handling multiple file selection in the FileDialog class
3.  Managing the Opacity of a Window
4.  Managing the Shape of a Window
5.  Managing Window types
6.  New border types in Java 7:RaisedSoftBevelBorder
7.  New border types in Java 7:LineBorder width
8.  New border types in Java 7:LoweredSoftBevelBorder
9.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED)
10.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
11.  Using the new JLayer Decorator for a password field
12.  Managing extra mouse buttons and high resolution mouse wheels
13.  Using the NumericShaper.Range enumeration to support the display of digits
