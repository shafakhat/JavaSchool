---
title: Java Swing Tutorial - Java Cursor CUSTOM_CURSOR
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Cursor.CUSTOM_CURSOR field.
section: Imported - java2s Archive
order: 1270
source: https://web.archive.org/web/20150325174927/http://www.java2s.com/Tutorials/Java/java.awt/Cursor/0060__Cursor.CUSTOM_CURSOR.htm
---
## Syntax

Cursor.CUSTOM_CURSOR has the following syntax.

```java title=Example.java
public static final int CUSTOM_CURSOR
```

## Example

In the following code shows how to use Cursor.CUSTOM_CURSOR field.

```java title=Example.java
import java.awt.Cursor;
import javax.swing.JFrame;
public class Main {
  public static void main(String[] args) {
    JFrame aWindow = new JFrame();
    aWindow.setBounds(200, 200, 200, 200);
    aWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    aWindow.setCursor(Cursor.getPredefinedCursor(Cursor.CUSTOM_CURSOR));
    aWindow.setVisible(true);
  }
}
java title=Example.java
```
