---
title: Java Swing Tutorial - Java BorderLayout AFTER_LAST_LINE
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BorderLayout.AFTER_LAST_LINE field.
section: Imported - java2s Archive
order: 1159
source: https://web.archive.org/web/20150325030953/http://www.java2s.com/Tutorials/Java/java.awt/BorderLayout/0040__BorderLayout.AFTER_LAST_LINE.htm
---
## Syntax

BorderLayout.AFTER_LAST_LINE has the following syntax.

```java title=Example.java
public static final String AFTER_LAST_LINE
```

## Example

In the following code shows how to use BorderLayout.AFTER_LAST_LINE field.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
public class Main {
  public static void main(String[] a) {
    JFrame frame = new JFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JPanel outerPanel = new JPanel(new BorderLayout());
    JPanel topPanel = new JPanel(new BorderLayout());
    JLabel label = new JLabel("Name:");
    JTextField text = new JTextField();
    topPanel.add(label, BorderLayout.BEFORE_LINE_BEGINS);
    topPanel.add(text, BorderLayout.CENTER);
    outerPanel.add(topPanel, BorderLayout.AFTER_LAST_LINE);
    frame.add(outerPanel);
    frame.setSize(300, 200);
    frame.setVisible(true);
  }
}
java title=Example.java
```
