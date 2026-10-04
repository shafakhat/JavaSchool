---
title: Java Swing Tutorial - Java FontMetrics.charWidth(char ch)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FontMetrics.charWidth(char ch) method.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FontMetrics/0120__FontMetrics.charWidth_char_ch_.htm
---
## Syntax

FontMetrics.charWidth(char ch) has the following syntax.

```java title=Example.java
publicint charWidth(char ch)
```

## Example

In the following code shows how to use FontMetrics.charWidth(char ch) method.

```java title=Example.java
import java.awt.FontMetrics;
import javax.swing.JFrame;
publicclass Main {
  publicstaticvoid main(String args[]) {
    JFrame f = new JFrame("JColorChooser Sample");
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setSize(300, 200);
    f.setVisible(true);
    FontMetrics metrics = f.getFontMetrics(f.getFont());
    int widthX = metrics.charWidth('X');
    System.out.println(widthX);
  }
}
```
