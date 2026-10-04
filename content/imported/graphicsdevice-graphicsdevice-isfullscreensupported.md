---
title: Java Swing Tutorial - Java GraphicsDevice .isFullScreenSupported ()
nav: Java Swing Tutorial - Java...
description: GraphicsDevice.isFullScreenSupported() has the following syntax.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsDevice/0320__GraphicsDevice.isFullScreenSupported_.htm
---
## Syntax

GraphicsDevice.isFullScreenSupported() has the following syntax.

```java title=Example.java
public boolean isFullScreenSupported()
```

## Example

In the following code shows how to use GraphicsDevice.isFullScreenSupported() method.

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.Window;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
public class Main extends Window {
  private BufferedImage pic;
  public static void main(String[] args) {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    GraphicsDevice screen = ge.getDefaultScreenDevice();
    if (!screen.isFullScreenSupported()) {
      System.out.println("Full screen mode not supported");
      System.exit(1);
    }
    try {
      BufferedImage loadedpic = ImageIO.read(new File("your.jpg"));
      screen.setFullScreenWindow(new Main (loadedpic));
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
  }
  public Main (BufferedImage pic) {
    super(new Frame());
    this.pic = pic;
    addMouseListener(new MouseAdapter() {
      public void mouseClicked(MouseEvent e) {
        System.exit(0);
      }
    });
  }
  public void paint(Graphics g) {
    g.drawImage(pic, 0, 0, getWidth(), getHeight(), this);
  }
}
```

The code above generates the following result.
