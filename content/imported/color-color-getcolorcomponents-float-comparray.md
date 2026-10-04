---
title: Java Swing Tutorial - Java Color .getColorComponents (float[] compArray)
nav: Java Swing Tutorial - Java...
description: Color.getColorComponents(float[] compArray) has the following syntax.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0920__Color.getColorComponents_float_compArray_.htm
---
## Syntax

Color.getColorComponents(float[] compArray) has the following syntax.

```java title=Example.java
public float[] getColorComponents(float[] compArray)
```

## Example

In the following code shows how to use Color.getColorComponents(float[] compArray) method.

```java title=Example.java
import java.awt.Color;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Color myColor = Color.RED;
    System.out.println(Arrays.toString(myColor.getColorComponents(null)));
  }
}
```

The code above generates the following result.
