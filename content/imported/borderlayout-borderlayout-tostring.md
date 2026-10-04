---
title: Java Swing Tutorial - Java BorderLayout.toString()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BorderLayout.toString() method.
section: Imported - java2s Archive
order: 1162
source: https://web.archive.org/web/20150325040614/http://www.java2s.com/Tutorials/Java/java.awt/BorderLayout/0680__BorderLayout.toString_.htm
---
## Syntax

BorderLayout.toString() has the following syntax.

```java title=Example.java
public String toString()
```

## Example

In the following code shows how to use BorderLayout.toString() method.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class Main  extends JPanel {
  public Main() {
    JButton btn1 = new JButton("Button1");
    JButton btn2 = new JButton("Button2");
    JButton btn3 = new JButton("Button3");
    JButton btn4 = new JButton("Button4");
    JButton btn5 = new JButton("Button5");
    JButton btn6 = new JButton("Button6");
    BorderLayout borderLayout = new BorderLayout(20,30);
    setLayout(borderLayout);
    add("North", btn1);
    add("West", btn2);
    add("Center", btn3);
    add("Center", btn4);
    add("South", btn5);
    add("East", btn6);
    System.out.println(borderLayout.toString());
  }
  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(400, 400);
    frame.setVisible(true);
  }
}
java title=Example.java
```
