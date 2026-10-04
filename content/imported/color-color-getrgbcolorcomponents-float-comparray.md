---
title: Java Swing Tutorial - Java Color .getRGBColorComponents (float[] compArray)
nav: Java Swing Tutorial - Java...
description: Color.getRGBColorComponents(float[] compArray) has the following syntax.
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/1080__Color.getRGBColorComponents_float_compArray_.htm
---
```java title=Example.java
Back to Color  ↑
```

## Syntax

Color.getRGBColorComponents(float[] compArray) has the following syntax.

```java title=Example.java
public float[] getRGBColorComponents(float[] compArray)
```

## Example

In the following code shows how to use Color.getRGBColorComponents(float[] compArray) method.

```java title=Example.java
import java.awt.Color;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    Color myColor = Color.RED;
    System.out.println(Arrays.toString(myColor.getRGBColorComponents(null)));
  }
}
```

The code above generates the following result.

- Back to Color ↑
