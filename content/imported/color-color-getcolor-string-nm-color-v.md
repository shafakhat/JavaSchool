---
title: Java Swing Tutorial - Java Color.getColor(String nm, Color v)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.getColor(String nm, Color v) method.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0860__Color.getColor_String_nm_Color_v_.htm
---
## Syntax

Color.getColor(String nm, Color v) has the following syntax.

```java title=Example.java
public static Color getColor(String nm,  Color v)
```

## Example

In the following code shows how to use Color.getColor(String nm, Color v) method.

```java title=Example.java
import java.awt.Color;
public class Main {
  public static void main(String[] args) {
    System.setProperty("myColor", "0XFFFFFF");
    Color myColor = Color.getColor("myColorNew",Color.RED);
    System.out.println(myColor);
  }
}
```

The code above generates the following result.
