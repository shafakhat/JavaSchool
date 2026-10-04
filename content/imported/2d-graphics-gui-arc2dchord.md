---
title: Arc2D.CHORD
nav: Arc2D.CHORD
description: Arc2D arc = new Arc2D.Float(200, 50, 100, 50, 0, 90, Arc2D.CHORD);
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20100212183135/http://java2s.com/Code/Java/2D-Graphics-GUI/Arc2DCHORD.htm
---
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
    Arc2D arc = new Arc2D.Float(200, 50, 100, 50, 0, 90, Arc2D.CHORD);
    g2d.draw(arc);
  }
}
```

1.  Draw draw an arc outline
---  ---
2.  Fill an arc outline
3.  Arc2D.Float: Arc2D.OPEN
4.  Arc2D.PIE
5.  Compares two arcs and returns true if they are equal or both null.
