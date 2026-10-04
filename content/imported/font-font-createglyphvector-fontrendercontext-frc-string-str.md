---
title: Java Swing Tutorial - Java Font .createGlyphVector (FontRenderContext frc, String str)
nav: Java Swing Tutorial - Java...
description: Font.createGlyphVector(FontRenderContext frc, String str) has the following syntax.
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/0720__Font.createGlyphVector_FontRenderContext_frc_String_str_.htm
---
## Syntax

Font.createGlyphVector(FontRenderContext frc, String str) has the following syntax.

```java title=Example.java
public GlyphVector createGlyphVector(FontRenderContext frc,    String str)
```

## Example

In the following code shows how to use Font.createGlyphVector(FontRenderContext frc, String str) method.

```java title=Example.java
import java.awt.Container;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.font.FontRenderContext;
import java.awt.font.GlyphVector;
import javax.swing.JComponent;
import javax.swing.JFrame;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JFrame jf = new JFrame("Demo");
    Container cp = jf.getContentPane();
    MyCanvas tl = new MyCanvas();
    cp.add(tl);
    jf.setSize(300, 200);
    jf.setVisible(true);
  }
}
class MyCanvas extends JComponent {
  publicvoid paint(Graphics g) {
    Graphics2D g2 = (Graphics2D)g;
    g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
        RenderingHints.VALUE_ANTIALIAS_ON);
    String s = "JavaSchool";
    Font font = new Font("Serif", Font.PLAIN, 24);
    FontRenderContext frc = g2.getFontRenderContext();
    GlyphVector gv = font.createGlyphVector(frc, s);
    g2.drawGlyphVector(gv, 40, 60);
  }
}
```
