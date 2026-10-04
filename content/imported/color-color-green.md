---
title: Java Swing Tutorial - Java Color green
nav: Java Swing Tutorial - Java...
description: Imported from the java2s.com archive: Java Swing Tutorial - Java Color green
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0240__Color.green.htm
---
```java title=Example.java
Back to Color  ↑
```

## Syntax

Color.green has the following syntax.

```java title=Example.java
publicstaticfinal Color green
```

## Example

In the following code shows how to use Color.green field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.green);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```

- Back to Color ↑
