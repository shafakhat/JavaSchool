---
title: Java Swing Tutorial - Java Color YELLOW
nav: Java Swing Tutorial - Java...
description: Imported from the java2s.com archive: Java Swing Tutorial - Java Color YELLOW
section: Imported - java2s Archive
order: 1243
source: https://web.archive.org/web/20150325173341/http://www.java2s.com/Tutorials/Java/java.awt/Color/0540__Color.YELLOW.htm
---
## Syntax

Color.YELLOW has the following syntax.

```java title=Example.java
public static final Color YELLOW
```

## Example

In the following code shows how to use Color.YELLOW field.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    JLabel label = new JLabel("First Name");
    label.setForeground(Color.YELLOW);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
java title=Example.java
```
