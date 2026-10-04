---
title: BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED)
nav: BorderFactory.createSoftBe...
description: panel.setBorder(BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED));
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20130223095852/http://www.java2s.com:80/Code/Java/JDK-7/BorderFactorycreateSoftBevelBorderBevelBorderLOWERED.htm
---
```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.BevelBorder;
public class Test extends JFrame {
  public static void main(String[] argv) {
    Test window = new Test();
    window.setVisible(true);
  }
  public Test() {
    this.setBounds(100, 100, 200, 100);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JPanel panel = new JPanel();
    panel.setBorder(BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED));
  //  panel.setBorder(BorderFactory.createSoftBevelBorder(BevelBorder.RAISED));
    this.setLayout(new FlowLayout());
    JButton exitButton = new JButton("Exit");
    panel.add(exitButton);
    this.add(panel);
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
3.  Managing the Opacity of a Window
4.  Managing the Shape of a Window
5.  Managing Window types
6.  Mixing heavyweight and lightweight components
7.  New border types in Java 7:RaisedSoftBevelBorder
8.  New border types in Java 7:LineBorder width
9.  New border types in Java 7:LoweredSoftBevelBorder
10.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
11.  Using the new JLayer Decorator for a password field
12.  Managing extra mouse buttons and high resolution mouse wheels
13.  Using the NumericShaper.Range enumeration to support the display of digits
