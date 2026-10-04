---
title: Java Swing Tutorial - Java Ellipse2D.hashCode()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Ellipse2D.hashCode() method.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Ellipse2D/0140__Ellipse2D.hashCode_.htm
---
```java title=Example.java
Back to Ellipse2D  ↑
```

## Syntax

Ellipse2D.hashCode() has the following syntax.

```java title=Example.java
publicint hashCode()
```

## Example

In the following code shows how to use Ellipse2D.hashCode() method.

```java title=Example.java
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
/*fromwww.java2s.com*/publicclass Main {

  publicstaticvoid main(String args[]) {
    Ellipse2D.Double e = new Ellipse2D.Double(1.0,2.0,2.0,2.0);

    System.out.println(e.hashCode());
  }
}
```

The code above generates the following result.

- Back to Ellipse2D ↑
