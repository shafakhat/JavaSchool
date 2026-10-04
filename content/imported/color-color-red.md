---
title: Java Swing Tutorial - Java Color RED
nav: Java Swing Tutorial - Java...
description: Imported from the java2s.com archive: Java Swing Tutorial - Java Color RED
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0460__Color.RED.htm
---
## Syntax

Color.RED has the following syntax.

```java title=Example.java
public static final Color RED
```

## Example

In the following code shows how to use Color.RED field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.RED);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```
