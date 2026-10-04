---
title: Java Swing Tutorial - Java FlowLayout LEADING
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FlowLayout.LEADING field.
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0060__FlowLayout.LEADING.htm
---
```java title=Example.java
Back to FlowLayout  ↑
```

## Syntax

FlowLayout.LEADING has the following syntax.

```java title=Example.java
publicstaticfinalint LEADING
```

## Example

In the following code shows how to use FlowLayout.LEADING field.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  public Main() {
    super(new FlowLayout(FlowLayout.LEADING, 10, 3));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
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

- Back to FlowLayout ↑
