---
title: Managing Window types
nav: Managing Window types
description: 10. BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
section: Imported - java2s Archive
order: 1098
source: https://web.archive.org/web/20130223095901/http://www.java2s.com:80/Code/Java/JDK-7/ManagingWindowtypes.htm
---
```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
public class Test extends JFrame {
  public static void main(String[] args) {
    Test window = new Test();
    window.setVisible(true);
  }
  public Test() {
    this.setBounds(100, 100, 200, 200);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setType(Type.UTILITY);
    this.setLayout(new FlowLayout());
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
3.  Managing the Opacity of a Window
4.  Managing the Shape of a Window
5.  Mixing heavyweight and lightweight components
6.  New border types in Java 7:RaisedSoftBevelBorder
7.  New border types in Java 7:LineBorder width
8.  New border types in Java 7:LoweredSoftBevelBorder
9.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED)
10.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
11.  Using the new JLayer Decorator for a password field
12.  Managing extra mouse buttons and high resolution mouse wheels
13.  Using the NumericShaper.Range enumeration to support the display of digits
