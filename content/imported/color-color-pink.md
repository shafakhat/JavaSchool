---
title: Java Swing Tutorial - Java Color PINK
nav: Java Swing Tutorial - Java...
description: Imported from the java2s.com archive: Java Swing Tutorial - Java Color PINK
section: Imported - java2s Archive
order: 1241
source: https://web.archive.org/web/20150325035717/http://www.java2s.com/Tutorials/Java/java.awt/Color/0420__Color.PINK.htm
---
## Syntax

Color.PINK has the following syntax.

```java title=Example.java
public static final Color PINK
```

## Example

In the following code shows how to use Color.PINK field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.PINK);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
java title=Example.java
```
