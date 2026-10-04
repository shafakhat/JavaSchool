---
title: Java Swing Tutorial - Java BasicStroke.getEndCap()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use BasicStroke.getEndCap() method.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/0340__BasicStroke.getEndCap_.htm
---
```java title=Example.java
Back to BasicStroke  ↑
```

## Example

In the following code shows how to use BasicStroke.getEndCap() method.

```java title=Example.java
//fromwww.java2s.comimport java.awt.BasicStroke;
import java.util.Arrays;

publicclass Main {
  publicstaticvoid main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(stroke.getEndCap());

  }
}
```

The code above generates the following result.

- Back to BasicStroke ↑
