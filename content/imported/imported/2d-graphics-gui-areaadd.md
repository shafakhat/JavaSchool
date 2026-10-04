---
title: Area Add
nav: Area Add
description: Area Add : Java examples (example source code) » 2D Graphics GUI » Area Calculation
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20060513101309/http://www.java2s.com/Code/Java/2D-Graphics-GUI/AreaAdd.htm
---
Area Add : Java examples (example source code) » 2D Graphics GUI » Area Calculation

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.geom.Area;
import java.awt.geom.Ellipse2D;
import javax.swing.JApplet;
import javax.swing.JFrame;
public class AreaAdd extends JApplet {
    Ellipse2D.Double circle = new Ellipse2D.Double();
    Ellipse2D.Double oval = new Ellipse2D.Double();
    Area circ = new Area(circle);
    Area ov = new Area(oval);
    public void init() {
        setBackground(Color.white);
    }
    public void paint (Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        double halfWdith = getSize().width/2;
        double halfHeight = getSize().height/2;
        circle.setFrame(halfWdith-25, halfHeight, 50.0, 50.0);
        oval.setFrame(halfWdith-19, halfHeight-20, 40.0, 70.0);
        circ = new Area(circle);
        ov = new Area(oval);
        circ.add(ov);
        g2.fill(circ);
    }
    public static void main(String s[]) {JFrame f = new JFrame("Pear");
        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {System.exit(0);}
        });
        JApplet applet = new AreaAdd();
        f.getContentPane().add("Center", applet);
        applet.init();
        f.pack();
        f.setSize(new Dimension(150,200));
        f.show();
    }
}
```

Related examples in the same category
---
1. Area Calculation: Add, Subtract, Intersect, Exclusive Or
2. Area Intersect
3. Area Subtract
4. Area Calculation: Add, Substract, XOR
