---
title: A quick utility to print out graphic device information
nav: A quick utility to print o...
description: By Marc Loy, Robert Eckstein, Dave Wood, James Elliott, Brian Cole
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20061026214845/http://www.java2s.com/Code/Java/2D-Graphics-GUI/Aquickutilitytoprintoutgraphicdeviceinformation.htm
---
A quick utility to print out graphic device information

```java title=Example.java
/*
Java Swing, 2nd Edition
By Marc Loy, Robert Eckstein, Dave Wood, James Elliott, Brian Cole
ISBN: 0-596-00408-7
Publisher: O'Reilly
*/
// GuiScreens.java
//A quick utility to print out graphic device information. Will work on
//systems with multiple monitors.
//
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.Rectangle;
import javax.swing.JFrame;
import javax.swing.JTextArea;
public class GuiScreens {
  public static void main(String[] args) {
    Rectangle virtualBounds = new Rectangle();
    GraphicsEnvironment ge = GraphicsEnvironment
        .getLocalGraphicsEnvironment();
    GraphicsDevice[] gs = ge.getScreenDevices();
    JFrame frame[][] = new JFrame[gs.length][];
    for (int j = 0; j < gs.length; j++) {
      GraphicsDevice gd = gs[j];
      System.out.println("Device " + j + ": " + gd);
      GraphicsConfiguration[] gc = gd.getConfigurations();
      frame[j] = new JFrame[gc.length];
      for (int i = 0; i < gc.length; i++) {
        System.out.println("  Configuration " + i + ": " + gc[i]);
        System.out.println("    Bounds: " + gc[i].getBounds());
        virtualBounds = virtualBounds.union(gc[i].getBounds());
        frame[j][i] = new JFrame("Config: " + i, gc[i]);
        frame[j][i].setBounds(50, 50, 400, 100);
        frame[j][i].setLocation((int) gc[i].getBounds().getX() + 50,
            (int) gc[i].getBounds().getY() + 50);
        frame[j][i].getContentPane().add(
            new JTextArea("Config:\n" + gc[i]));
        frame[j][i].setVisible(true);
      }
      System.out.println("Overall bounds: " + virtualBounds);
    }
  }
}
```

Related examples in the same category
---
1. List all available fonts provied in the system
2. Show all fonts you have in your system
3. Get the GraphicsEnvironment and GraphicsDevice
