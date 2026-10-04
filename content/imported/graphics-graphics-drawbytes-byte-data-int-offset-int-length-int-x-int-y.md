---
title: Java Swing Tutorial - Java Graphics.drawBytes(byte[] data, int offset, int length, int x, int y)
nav: Java Swing Tutorial - Java...
description: Graphics.drawBytes(byte[] data, int offset, int length, int x, int y) has the following syntax.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0220__Graphics.drawBytes_byte_data_int_offset_int_length_int_x_int_y_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.drawBytes(byte[] data, int offset, int length, int x, int y) has the following syntax.

```java title=Example.java
publicvoid drawBytes(byte[] data,  int offset,  int length,  int x,  int y)
```

## Example

In the following code shows how to use Graphics.drawBytes(byte[] data, int offset, int length, int x, int y) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    byte [] barray = { 0x41, 0x42, 0x43 };
    g.drawBytes (barray, 0, barray.length, 10, 30);
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
