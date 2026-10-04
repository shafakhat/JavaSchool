---
title: Java Swing Tutorial - Java Cursor MOVE_CURSOR
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Cursor.MOVE_CURSOR field.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Cursor/0140__Cursor.MOVE_CURSOR.htm
---
## Syntax

Cursor.MOVE_CURSOR has the following syntax.

```java title=Example.java
public static final int MOVE_CURSOR
```

## Example

In the following code shows how to use Cursor.MOVE_CURSOR field.

```java title=Example.java
import java.awt.Cursor;
import javax.swing.JFrame;
public class Main {
  public static void main(String[] args) {
    JFrame aWindow = new JFrame();
    aWindow.setBounds(200, 200, 200, 200);
    aWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    aWindow.setCursor(Cursor.getPredefinedCursor(Cursor.MOVE_CURSOR));
    aWindow.setVisible(true);
  }
}
```
