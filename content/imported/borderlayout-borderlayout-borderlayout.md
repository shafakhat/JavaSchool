---
title: Java Swing Tutorial - Java BorderLayout() Constructor
nav: Java Swing Tutorial - Java...
description: BorderLayout() constructor from BorderLayout has the following syntax.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BorderLayout/0300__BorderLayout.BorderLayout_.htm
---
```java title=Example.java
Back to BorderLayout  ↑
```

## Syntax

BorderLayout() constructor from BorderLayout has the following syntax.

```java title=Example.java
public BorderLayout()
```

## Example

In the following code shows how to use BorderLayout.BorderLayout() constructor.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main  extends JPanel {
  public Main() {
    JButton btn1 = new JButton("Button1");
    JButton btn2 = new JButton("Button2");
    JButton btn3 = new JButton("Button3");
    JButton btn4 = new JButton("Button4");
    JButton btn5 = new JButton("Button5");
    JButton btn6 = new JButton("Button6");
    setLayout(new BorderLayout());
    add("North", btn1);
    add("West", btn2);
    add("Center", btn3);
    add("Center", btn4);
    add("South", btn5);
    add("East", btn6);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```

- Back to BorderLayout ↑
