---
title: Java Swing Tutorial - Java Color(float r, float g, float b, float a) Constructor
nav: Java Swing Tutorial - Java...
description: Color(float r, float g, float b, float a) constructor from Color has the following syntax.
section: Imported - java2s Archive
order: 1230
source: https://web.archive.org/web/20150325164816/http://www.java2s.com/Tutorials/Java/java.awt/Color/0600__Color.Color_float_r_float_g_float_b_float_a_.htm
---
## Syntax

Color(float r, float g, float b, float a) constructor from Color has the following syntax.

```java title=Example.java
public Color(float r,  float g,  float b,  float a)
```

## Example

In the following code shows how to use Color.Color(float r, float g, float b, float a) constructor.

```java title=Example.java
import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JLabel;
public class Main {
  public static void main(String[] args) {
    Color myBlack = new Color(0,0,0,0.5F);           // Color black
//  Color myWhite = new Color(255,255,255);     // Color white
//  Color myGreen = new Color(0,200,0);         // A shade of green
    JLabel label = new JLabel("First Name");
    label.setForeground(myBlack);
    JFrame frame = new JFrame();
    frame.add(label);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setBounds(20,20, 500,500);
    frame.setVisible(true);
  }
}
java title=Example.java
```
