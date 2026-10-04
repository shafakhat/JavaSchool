---
title: Java Swing Tutorial - Java Graphics.getClip()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Graphics.getClip() method.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics/0720__Graphics.getClip_.htm
---
```java title=Example.java
Back to Graphics  ↑
```

## Syntax

Graphics.getClip() has the following syntax.

```java title=Example.java
publicabstract Shape getClip()
```

## Example

In the following code shows how to use Graphics.getClip() method.

```java title=Example.java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    g.drawString(g.getClip()+"", 10, 30);
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
