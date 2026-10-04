---
title: Java Swing Tutorial - Java Color magenta
nav: Java Swing Tutorial - Java...
description: Imported from the java2s.com archive: Java Swing Tutorial - Java Color magenta
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0320__Color.magenta.htm
---
## Syntax

Color.magenta has the following syntax.

```java title=Example.java
publicstaticfinal Color magenta
```

## Example

In the following code shows how to use Color.magenta field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
publicclass Main {
  publicstaticvoid main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.magenta);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```
