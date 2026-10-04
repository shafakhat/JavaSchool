---
title: Java Swing Tutorial - Java Color.HSBtoRGB(float hue, float saturation, float brightness)
nav: Java Swing Tutorial - Java...
description: Color.HSBtoRGB(float hue, float saturation, float brightness) has the following syntax.
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/1160__Color.HSBtoRGB_float_hue_float_saturation_float_brightness_.htm
---
## Syntax

Color.HSBtoRGB(float hue, float saturation, float brightness) has the following syntax.

```java title=Example.java
publicstaticint HSBtoRGB(float hue,  float saturation,  float brightness)
```

## Example

In the following code shows how to use Color.HSBtoRGB(float hue, float saturation, float brightness) method.

```java title=Example.java
import java.awt.Color;
publicclass Main {
  publicstaticvoid main(String[] args) {
    int rgb = Color.HSBtoRGB(1.0f, 1.0f, 1.0f);
    System.out.println(rgb);
  }
}
```

The code above generates the following result.
