---
title: Java Swing Tutorial - Java FlowLayout CENTER
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FlowLayout.CENTER field.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0040__FlowLayout.CENTER.htm
---
## Syntax

FlowLayout.CENTER has the following syntax.

```java title=Example.java
public static final int CENTER
```

## Example

In the following code shows how to use FlowLayout.CENTER field.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main extends JPanel {
  public Main() {
    super(new FlowLayout(FlowLayout.CENTER, 10, 3));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
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
