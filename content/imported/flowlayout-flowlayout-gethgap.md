---
title: Java Swing Tutorial - Java FlowLayout.getHgap()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FlowLayout.getHgap() method.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0260__FlowLayout.getHgap_.htm
---
## Syntax

FlowLayout.getHgap() has the following syntax.

```java title=Example.java
publicint getHgap()
```

## Example

In the following code shows how to use FlowLayout.getHgap() method.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  public Main() {
    FlowLayout flowLayout = new FlowLayout(FlowLayout.RIGHT, 10, 3);
    setLayout(flowLayout);
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    System.out.println(flowLayout.getHgap());
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```
