---
title: Java Swing Tutorial - Java Graphics.drawChars(char[] data, int offset, int length, int x, int y)
nav: Java Swing Tutorial - Java...
description: Graphics.drawChars(char[] data, int offset, int length, int x, int y) has the following syntax.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0240__Graphics.drawChars_char_data_int_offset_int_length_int_x_int_y_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.drawChars(char[] data, int offset, int length, int x, int y) has the following syntax.

```java title=Example.java
publicvoid drawChars(char[] data,  int offset,  int length,  int x,  int y)
```

## Example

In the following code shows how to use Graphics.drawChars(char[] data, int offset, int length, int x, int y) method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    char [] carray = { 'w', 'w', 'w','.', 'j','a','v','a','2','s','.','c','o','m'};
    g.drawChars (carray, 0, carray.length, 10, 60);
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
