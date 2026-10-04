---
title: Java Swing Tutorial - Java Color lightGray
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.lightGray field.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0300__Color.lightGray.htm
---
## Syntax

Color.lightGray has the following syntax.

```java title=Example.java
public static final Color lightGray
```

## Example

In the following code shows how to use Color.lightGray field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.lightGray);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
```
