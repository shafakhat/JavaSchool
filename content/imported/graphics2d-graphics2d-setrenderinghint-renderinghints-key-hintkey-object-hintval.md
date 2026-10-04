---
title: Java Swing Tutorial - Java Graphics2D .setRenderingHint (RenderingHints .Key hintKey, Object hintValue)
nav: Java Swing Tutorial - Java...
description: Graphics2D.setRenderingHint(RenderingHints.Key hintKey, Object hintValue) has the following syntax.
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Graphics2D/0680__Graphics2D.setRenderingHint_RenderingHints_Key_hintKey_Object_hintValue_.htm
---
## Syntax

Graphics2D.setRenderingHint(RenderingHints.Key hintKey, Object hintValue) has the following syntax.

```java title=Example.java
publicabstractvoid setRenderingHint(RenderingHints.Key hintKey,   Object hintValue)
```

## Example

In the following code shows how to use Graphics2D.setRenderingHint(RenderingHints.Key hintKey, Object hintValue) method.

```java title=Example.java
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D)g;
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
        RenderingHints.VALUE_ANTIALIAS_ON);
    Font font = new Font("Serif", Font.PLAIN, 96);
    g2.setFont(font);
    g2.drawString("jade", 40, 120);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20, 20, 500, 500);
    frame.setVisible(true);
  }
}
```
