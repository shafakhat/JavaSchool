---
title: AlphaComposite.SRC_OUT
nav: AlphaComposite.SRC_OUT
description: AlphaComposite ac = AlphaComposite.getInstance(AlphaComposite.SRC_OUT, 0.5f);
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20090502012708/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/AlphaCompositeSRCOUT.htm
---
AlphaComposite.SRC_OUT

```java title=Example.java
import java.awt.AlphaComposite;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class CompositingDST_ATOP extends JPanel {
  public void paint(Graphics g) {
    Graphics2D g2d = (Graphics2D) g;
    AlphaComposite ac = AlphaComposite.getInstance(AlphaComposite.SRC_OUT, 0.5f);
    BufferedImage buffImg = new BufferedImage(60, 60, BufferedImage.TYPE_INT_ARGB);
    Graphics2D gbi = buffImg.createGraphics();
    gbi.setPaint(Color.red);
    gbi.fillRect(0, 0, 40, 40);
    gbi.setComposite(ac);
    gbi.setPaint(Color.green);
    gbi.fillRect(5, 5, 40, 40);
    g2d.drawImage(buffImg, 20, 20, null);
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame("Composition");
    frame.add(new CompositingDST_ATOP());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(400, 120);
    frame.setVisible(true);
  }
}
```

1.  Composite demo
---  ---
2.  AlphaComposite
3.  AlphaComposite.DST
4.  AlphaComposite.DST_ATOP
5.  AlphaComposite.DST_OUT
6.  AlphaComposite.SRC
7.  AlphaComposite.SRC_ATOP
8.  Composite Effects
9.  Composite Test
10.  Blend Composite Demo
