---
title: Java Swing Tutorial - Java FontMetrics.bytesWidth(byte[] data, int off, int len)
nav: Java Swing Tutorial - Java...
description: FontMetrics.bytesWidth(byte[] data, int off, int len) has the following syntax.
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FontMetrics/0080__FontMetrics.bytesWidth_byte_data_int_off_int_len_.htm
---
```java title=Example.java
Back to FontMetrics  ↑
```

## Syntax

FontMetrics.bytesWidth(byte[] data, int off, int len) has the following syntax.

```java title=Example.java
publicint bytesWidth(byte[] data,  int off,  int len)
```

## Example

In the following code shows how to use FontMetrics.bytesWidth(byte[] data, int off, int len) method.

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
    int widthX = metrics.bytesWidth(newbyte[]{66, 67, 68,69}, 1,2);
    System.out.println(widthX);
  }
}
```

- Back to FontMetrics ↑
