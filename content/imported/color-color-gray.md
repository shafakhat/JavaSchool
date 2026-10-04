---
title: Java Swing Tutorial - Java Color GRAY
nav: Java Swing Tutorial - Java...
description: //from w w w . j a v a2 s. c o mimport javax.swing.JFrame;
section: Imported - java2s Archive
order: 1251
source: https://web.archive.org/web/20150325171828/http://www.java2s.com/Tutorials/Java/java.awt/Color/0220__Color.GRAY.htm
---
## Syntax

Color.GRAY has the following syntax.

```java title=Example.java
public static final Color GRAY
```

## Example

In the following code shows how to use Color.GRAY field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.GRAY);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
java title=Example.java
```
