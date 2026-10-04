---
title: Java Swing Tutorial - Java FlowLayout.setVgap(int vgap)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FlowLayout.setVgap(int vgap) method.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0440__FlowLayout.setVgap_int_vgap_.htm
---
## Syntax

FlowLayout.setVgap(int vgap) has the following syntax.

```java title=Example.java
public void setVgap(int vgap)
```

## Example

In the following code shows how to use FlowLayout.setVgap(int vgap) method.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public Main() {
    FlowLayout flowLayout = new FlowLayout(FlowLayout.RIGHT, 10, 3);
    setLayout(flowLayout);
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    flowLayout.setHgap(10);
    flowLayout.setVgap(12);
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```
