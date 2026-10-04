---
title: Managing extra mouse buttons and high resolution mouse wheels
nav: Managing extra mouse butto...
description: Managing extra mouse buttons and high resolution mouse wheels
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20130223094553/http://www.java2s.com:80/Code/Java/JDK-7/Managingextramousebuttonsandhighresolutionmousewheels.htm
---
Managing extra mouse buttons and high resolution mouse wheels

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.MouseInfo;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;
import javax.swing.JButton;
import javax.swing.JFrame;
public class Test {
  public static void main(String[] args) {
    ApplicationWindow window = new ApplicationWindow();
    window.setVisible(true);
  }
}
class ApplicationWindow extends JFrame implements MouseListener,
    MouseWheelListener {
  public ApplicationWindow() {
    this.setSize(200, 100);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setLayout(new FlowLayout());
    JButton exitButton = new JButton("Exit");
    this.add(exitButton);
    int totalButtons = MouseInfo.getNumberOfButtons();
    System.out.println(Toolkit.getDefaultToolkit()
        .areExtraMouseButtonsEnabled());
    System.out.println("You have " + totalButtons + " total buttons");
    this.addMouseListener(this);
    this.addMouseWheelListener(this);
    exitButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        System.exit(0);
      }
    });
  }
  public void mousePressed(MouseEvent e) {
    System.out.println("" + e.getButton());
  }
  public void mouseWheelMoved(MouseWheelEvent e) {
    System.out.println("" + e.getPreciseWheelRotation() + " - "
        + e.getWheelRotation());
  }
  @Override
  public void mouseClicked(MouseEvent e) {
  }
  @Override
  public void mouseReleased(MouseEvent e) {
  }
  @Override
  public void mouseEntered(MouseEvent e) {
  }
  @Override
  public void mouseExited(MouseEvent e) {
    throw new UnsupportedOperationException("Not supported yet.");
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
10.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED)
11.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
12.  Using the new JLayer Decorator for a password field
13.  Using the NumericShaper.Range enumeration to support the display of digits
