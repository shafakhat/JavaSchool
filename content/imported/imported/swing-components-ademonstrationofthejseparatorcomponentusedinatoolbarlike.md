---
title: A demonstration of the JSeparator() component used in a toolbar-like
nav: A demonstration of the JSe...
description: A demonstration of the JSeparator() component used in a toolbar-like : Java examples (example source code) » Swing Components » Separator
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20060523170346/http://www.java2s.com:80/Code/Java/Swing-Components/AdemonstrationoftheJSeparatorcomponentusedinatoolbarlike.htm
---
A demonstration of the JSeparator() component used in a toolbar-like : Java examples (example source code) » Swing Components » Separator

```java title=Example.java
/*
Java Swing, 2nd Edition
By Marc Loy, Robert Eckstein, Dave Wood, James Elliott, Brian Cole
ISBN: 0-596-00408-7
Publisher: O'Reilly
*/
// SeparatorExample.java
// A quick demonstration of the JSeparator() component used in a toolbar-like
// container.
//
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JSeparator;
public class SeparatorExample extends JPanel {
  public SeparatorExample() {
    super(true);
    setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
    Box box1 = new Box(BoxLayout.X_AXIS);
    Box box2 = new Box(BoxLayout.X_AXIS);
    Box box3 = new Box(BoxLayout.X_AXIS);
    box1.add(new JButton("Press Me"));
    box1.add(new JButton("No Me!"));
    box1.add(new JButton("Ignore Them!"));
    box2.add(new JSeparator());
    box3.add(new JButton("I'm the Button!"));
    box3.add(new JButton("It's me!"));
    box3.add(new JButton("Go Away!"));
    add(box1);
    add(box2);
    add(box3);
  }
  public static void main(String s[]) {
    SeparatorExample example = new SeparatorExample();
    JFrame frame = new JFrame("Separator Example");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setContentPane(example);
    frame.pack();
    frame.setVisible(true);
  }
}
```

Related examples in the same category
---
1. Separator Sample
2. Separator Sample 2
