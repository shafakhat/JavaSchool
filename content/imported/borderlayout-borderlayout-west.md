---
title: Java Swing Tutorial - Java BorderLayout WEST
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BorderLayout.WEST field.
section: Imported - java2s Archive
order: 1163
source: https://web.archive.org/web/20150325172515/http://www.java2s.com/Tutorials/Java/java.awt/BorderLayout/0280__BorderLayout.WEST.htm
---
## Syntax

BorderLayout.WEST has the following syntax.

```java title=Example.java
public static final String WEST
```

## Example

In the following code shows how to use BorderLayout.WEST field.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JToggleButton;
public class Main {
  public static void main(String args[]) {
    JFrame f = new JFrame("JToggleButton Sample");
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.add(new JToggleButton("North"), BorderLayout.NORTH);
    f.add(new JToggleButton("East"), BorderLayout.EAST);
    f.add(new JToggleButton("West"), BorderLayout.WEST);
    f.add(new JToggleButton("Center"), BorderLayout.CENTER);
    f.add(new JToggleButton("South"), BorderLayout.SOUTH);
    f.setSize(300, 200);
    f.setVisible(true);
  }
}
java title=Example.java
```
