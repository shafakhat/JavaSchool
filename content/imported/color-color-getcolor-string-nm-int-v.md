---
title: Java Swing Tutorial - Java Color.getColor(String nm, int v)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.getColor(String nm, int v) method.
section: Imported - java2s Archive
order: 1231
source: https://web.archive.org/web/20150325035548/http://www.java2s.com/Tutorials/Java/java.awt/Color/0880__Color.getColor_String_nm_int_v_.htm
---
## Syntax

Color.getColor(String nm, int v) has the following syntax.

```java title=Example.java
public static Color getColor(String nm,  int v)
```

## Example

In the following code shows how to use Color.getColor(String nm, int v) method.

```java title=Example.java
import java.awt.Color;
public class Main {
  public static void main(String[] args) {
    System.setProperty("myColor", "0XFFFFFF");
    Color myColor = Color.getColor("myColorNew",0XFF00FF);
    System.out.println(myColor);
  }
}
```

The code above generates the following result.
