---
title: Java Swing Tutorial - Java BasicStroke.equals(Object obj)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.equals(Object obj) method.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0280__BasicStroke.equals_Object_obj_.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Syntax

BasicStroke.equals(Object obj) has the following syntax.

```java title=Example.java
publicboolean equals(Object obj)
```

## Example

In the following code shows how to use BasicStroke.equals(Object obj) method.

```java title=Example.java
import java.awt.BasicStroke;
publicclass Main {
  publicstaticvoid main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(stroke.equals(stroke));
  }
}
```

The code above generates the following result.

- Back to BasicStroke ↑
