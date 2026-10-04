---
title: Arc2D.PIE
nav: Arc2D.PIE
description: Arc2D arc = new Arc2D.Float(200, 50, 100, 50, 0, 90, Arc2D.PIE);
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20090523115257/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Arc2DPIE.htm
---
Arc2D.PIE

```java title=Example.java
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Arc2D;
public class MainClass extends Frame {
  public static void main(String[] args) {
    (new MainClass()).setVisible(true);
  }
  public MainClass() {
    super("Shape Sampler");
    setSize(400, 550);
  }
  public void paint(Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    Arc2D arc = new Arc2D.Float(200, 50, 100, 50, 0, 90, Arc2D.PIE);
    g2d.draw(arc);
  }
}
```

1.  Draw draw an arc outline
---  ---
2.  Fill an arc outline
3.  Arc2D.Float: Arc2D.OPEN
4.  Arc2D.CHORD
