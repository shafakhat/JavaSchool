---
title: Java Swing Tutorial - Java Color blue
nav: Java Swing Tutorial - Java...
description: Imported from the java2s.com archive: Java Swing Tutorial - Java Color blue
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0080__Color.blue.htm
---
```java title=Example.java
Back to Color  ↑
```

## Syntax

Color.blue has the following syntax.

```java title=Example.java
publicstaticfinal Color blue
```

## Example

In the following code shows how to use Color.blue field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.blue);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

- Back to Color ↑
