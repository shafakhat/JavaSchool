---
title: Java Swing Tutorial - Java BasicStroke.getLineJoin()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.getLineJoin() method.
section: Imported - java2s Archive
order: 1141
source: https://web.archive.org/web/20150325073206/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0360__BasicStroke.getLineJoin_.htm
---
## Syntax

BasicStroke.getLineJoin() has the following syntax.

```java title=Example.java
public int getLineJoin()
```

## Example

In the following code shows how to use BasicStroke.getLineJoin() method.

```java title=Example.java
import java.awt.BasicStroke;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(stroke.getLineJoin());
  }
}
```

The code above generates the following result.
