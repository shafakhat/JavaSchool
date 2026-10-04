---
title: Java Swing Tutorial - Java FlowLayout .setAlignOnBaseline (boolean alignOnBaseline)
nav: Java Swing Tutorial - Java...
description: FlowLayout.setAlignOnBaseline(boolean alignOnBaseline) has the following syntax.
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/FlowLayout/0400__FlowLayout.setAlignOnBaseline_boolean_alignOnBaseline_.htm
---
```java title=Example.java
Back to FlowLayout  ↑
```

## Syntax

FlowLayout.setAlignOnBaseline(boolean alignOnBaseline) has the following syntax.

```java title=Example.java
publicvoid setAlignOnBaseline(boolean alignOnBaseline)
```

## Example

In the following code shows how to use FlowLayout.setAlignOnBaseline(boolean alignOnBaseline) method.

```java title=Example.java
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extends JPanel {
  public Main() {
    FlowLayout flowLayout = new FlowLayout(FlowLayout.RIGHT, 10, 3);
    setLayout(flowLayout);
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    add(new JButton("JavaSchool"));
    flowLayout.setAlignOnBaseline(false);
  }
  publicstaticvoid main(String[] args) {
    JFrame frame = new JFrame();
    frame.add(new Main());
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}
```

- Back to FlowLayout ↑
