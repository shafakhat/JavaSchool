---
title: Java Swing Tutorial - Java BasicStroke.getLineWidth()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.getLineWidth() method.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0380__BasicStroke.getLineWidth_.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Syntax

BasicStroke.getLineWidth() has the following syntax.

```java title=Example.java
public float getLineWidth()
```

## Example

In the following code shows how to use BasicStroke.getLineWidth() method.

```java title=Example.java
import java.awt.BasicStroke;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(stroke.getLineWidth());
  }
}
```

The code above generates the following result.

- Back to BasicStroke ↑
