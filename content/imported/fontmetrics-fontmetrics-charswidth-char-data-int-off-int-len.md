---
title: Java Swing Tutorial - Java FontMetrics.charsWidth(char[] data, int off, int len)
nav: Java Swing Tutorial - Java...
description: FontMetrics.charsWidth(char[] data, int off, int len) has the following syntax.
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FontMetrics/0100__FontMetrics.charsWidth_char_data_int_off_int_len_.htm
---
```java title=Example.java
Back to FontMetrics  ↑
```

## Syntax

FontMetrics.charsWidth(char[] data, int off, int len) has the following syntax.

```java title=Example.java
publicint charsWidth(char[] data,  int off,  int len)
```

## Example

In the following code shows how to use FontMetrics.charsWidth(char[] data, int off, int len) method.

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
    int widthX = metrics.charsWidth(newchar[]{'a','b'}, 1,2);
    System.out.println(widthX);
  }
}
```

- Back to FontMetrics ↑
