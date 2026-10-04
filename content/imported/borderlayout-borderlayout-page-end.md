---
title: Java Swing Tutorial - Java BorderLayout PAGE_END
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BorderLayout.PAGE_END field.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BorderLayout/0220__BorderLayout.PAGE_END.htm
---
```java title=Example.java
Back to BorderLayout  ↑
```

## Syntax

BorderLayout.PAGE_END has the following syntax.

```java title=Example.java
publicstaticfinal String PAGE_END
```

## Example

In the following code shows how to use BorderLayout.PAGE_END field.

```java title=Example.java
import java.awt.BorderLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
publicclass Main {
  publicstaticvoid main(String[] a) {
    JFrame frame = new JFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JPanel outerPanel = new JPanel(new BorderLayout());
    JPanel topPanel = new JPanel(new BorderLayout());
    JLabel label = new JLabel("Name:");
    JTextField text = new JTextField();
    topPanel.add(label, BorderLayout.PAGE_END);
    topPanel.add(text, BorderLayout.CENTER);
    outerPanel.add(topPanel, BorderLayout.AFTER_LAST_LINE);
    frame.add(outerPanel);
    frame.setSize(300, 200);
    frame.setVisible(true);
  }
}
```

- Back to BorderLayout ↑
