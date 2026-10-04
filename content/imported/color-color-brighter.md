---
title: Java Swing Tutorial - Java Color.brighter()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.brighter() method.
section: Imported - java2s Archive
order: 1229
source: https://web.archive.org/web/20150325033136/http://www.java2s.com/Tutorials/Java/java.awt/Color/0700__Color.brighter_.htm
---
## Syntax

Color.brighter() has the following syntax.

```java title=Example.java
public Color brighter()
```

## Example

In the following code shows how to use Color.brighter() method.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    Color myColor = Color.RED;
    JLabel label = new JLabel("First Name");
    label.setForeground(myColor.brighter());
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
java title=Example.java
```
