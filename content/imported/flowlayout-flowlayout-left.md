---
title: Java Swing Tutorial - Java FlowLayout LEFT
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use FlowLayout.LEFT field.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0080__FlowLayout.LEFT.htm
---
```java title=Example.java
Back to FlowLayout  ↑
```

## Syntax

FlowLayout.LEFT has the following syntax.

```java title=Example.java
publicstaticfinalint LEFT
```

## Example

In the following code shows how to use FlowLayout.LEFT field.

```java title=Example.java
import java.awt.Container;
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JFrame aWindow = new JFrame();
    aWindow.setBounds(200, 200, 200, 200);
    aWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    Container content = aWindow.getContentPane();
    content.setLayout(new FlowLayout(FlowLayout.LEFT));
    content.add(new JButton("JavaSchool"));
    content.add(new JLabel("JavaSchool"));
    content.add(new JTextField("JavaSchool"));
    aWindow.setVisible(true);
  }
}
```

- Back to FlowLayout ↑
