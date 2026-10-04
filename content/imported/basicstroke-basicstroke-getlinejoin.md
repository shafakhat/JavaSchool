---
title: Java Swing Tutorial - Java BasicStroke.getLineJoin()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.getLineJoin() method.
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0360__BasicStroke.getLineJoin_.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Syntax

BasicStroke.getLineJoin() has the following syntax.

```java title=Example.java
publicint getLineJoin()
```

## Example

In the following code shows how to use BasicStroke.getLineJoin() method.

```java title=Example.java
import java.awt.BasicStroke;
import java.util.Arrays;
publicclass Main {
  publicstaticvoid main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(stroke.getLineJoin());
  }
}
```

The code above generates the following result.

- Back to BasicStroke ↑
