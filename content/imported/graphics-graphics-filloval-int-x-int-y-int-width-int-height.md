---
title: Java Swing Tutorial - Java Graphics.fillOval(int x, int y, int width, int height)
nav: Java Swing Tutorial - Java...
description: Graphics.fillOval(int x, int y, int width, int height) has the following syntax.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0600__Graphics.fillOval_int_x_int_y_int_width_int_height_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.fillOval(int x, int y, int width, int height) has the following syntax.

```java title=Example.java
publicabstractvoid fillOval(int x,  int y,  int width,  int height)
```

## Example

In the following code shows how to use Graphics.fillOval(int x, int y, int width, int height) method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.fillOval(25, 25, 120, 120);
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
