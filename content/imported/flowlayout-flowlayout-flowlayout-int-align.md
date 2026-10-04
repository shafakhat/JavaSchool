---
title: Java Swing Tutorial - Java FlowLayout(int align) Constructor
nav: Java Swing Tutorial - Java...
description: FlowLayout(int align) constructor from FlowLayout has the following syntax.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0160__FlowLayout.FlowLayout_int_align_.htm
---
```java title=Example.java
Back to FlowLayout  ↑
```

## Syntax

FlowLayout(int align) constructor from FlowLayout has the following syntax.

```java title=Example.java
public FlowLayout(int align)
```

## Example

In the following code shows how to use FlowLayout.FlowLayout(int align) constructor.

```java title=Example.java
import java.awt.Container;
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
publicclass Main extends JFrame {
  publicstaticvoid main(String[] args) {
    Main ft = new Main();
    ft.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    ft.setSize(400, 300);
    ft.setVisible(true);
  }
  public Main() {
    super();
    Container pane = getContentPane();
    pane.setLayout(new FlowLayout(FlowLayout.LEFT));
    pane.add(new JLabel("This is a test"));
    pane.add(new JButton("of a FlowLayout"));
    pane.add(new JTextField(30));
    pane.add(new JTextArea("This is a JTextArea", 3, 10));
    pane.add(new JLabel("This is a FlowLayout test with a long string"));
  }
}
```

- Back to FlowLayout ↑
