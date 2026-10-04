---
title: Java Swing Tutorial - Java Graphics.drawString(String str, int x, int y)
nav: Java Swing Tutorial - Java...
description: Graphics.drawString(String str, int x, int y) has the following syntax.
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0540__Graphics.drawString_String_str_int_x_int_y_.htm
---
## Syntax

Graphics.drawString(String str, int x, int y) has the following syntax.

```java title=Example.java
public abstract void drawString(String str,  int x,  int y)
```

## Example

In the following code shows how to use Graphics.drawString(String str, int x, int y) method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public void paint(Graphics g) {
    int fontSize = 20;
    g.setFont(new Font("TimesRoman", Font.PLAIN, fontSize));
    g.drawString("JavaSchool", 10, 20);
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```
