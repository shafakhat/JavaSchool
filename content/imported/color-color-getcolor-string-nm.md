---
title: Java Swing Tutorial - Java Color.getColor(String nm)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.getColor(String nm) method.
section: Imported - java2s Archive
order: 1235
source: https://web.archive.org/web/20150325035909/http://www.java2s.com/Tutorials/Java/java.awt/Color/0840__Color.getColor_String_nm_.htm
---
## Syntax

Color.getColor(String nm) has the following syntax.

```java title=Example.java
public static Color getColor(String nm)
```

## Example

In the following code shows how to use Color.getColor(String nm) method.

```java title=Example.java
import java.awt.Color;
public class Main {
  public static void main(String[] args) {
    System.setProperty("myColor", "0XFFFFFF");
    Color myColor = Color.getColor("myColor");
    System.out.println(myColor);
  }
}
```

The code above generates the following result.
