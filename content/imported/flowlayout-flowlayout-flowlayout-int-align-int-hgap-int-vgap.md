---
title: Java Swing Tutorial - Java FlowLayout(int align, int hgap, int vgap) Constructor
nav: Java Swing Tutorial - Java...
description: FlowLayout(int align, int hgap, int vgap) constructor from FlowLayout has the following syntax.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0180__FlowLayout.FlowLayout_int_align_int_hgap_int_vgap_.htm
---
## Syntax

FlowLayout(int align, int hgap, int vgap) constructor from FlowLayout has the following syntax.

```java title=Example.java
public FlowLayout(int align,   int hgap,   int vgap)
```

## Example

In the following code shows how to use FlowLayout.FlowLayout(int align, int hgap, int vgap) constructor.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public Main() {
    super(new FlowLayout(FlowLayout.RIGHT, 10, 3));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```
