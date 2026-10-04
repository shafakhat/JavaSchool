---
title: Java Swing Tutorial - Java Graphics.drawImage(Image img, int x, int y, int width, int height, ImageObserver observer)
nav: Java Swing Tutorial - Java...
description: Graphics.drawImage(Image img, int x, int y, int width, int height, ImageObserver observer) has the following syntax.
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0320__Graphics.drawImage_Image_img_int_x_int_y_int_width_int_height_ImageObserver_observer_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.drawImage(Image img, int x, int y, int width, int height, ImageObserver observer) has the following syntax.

```java title=Example.java
publicabstractboolean drawImage(Image img,  int x,  int y,  int width,  int height,   ImageObserver observer)
```

## Example

In the following code shows how to use Graphics.drawImage(Image img, int x, int y, int width, int height, ImageObserver observer) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Image img = createImage();
    g.drawImage(img, 20,20,400,400,this);
  }
  private Image createImage(){
    BufferedImage bufferedImage = new BufferedImage(200,200,BufferedImage.TYPE_INT_RGB);
    Graphics g = bufferedImage.getGraphics();
    g.drawString("JavaSchool", 20,20);
    return bufferedImage;
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

- Back to Graphics ↑
