---
title: Java Tutorial - Java Ellipse2D() Constructor
nav: Java Tutorial - Java Ellip...
description: Ellipse2D() constructor from Ellipse2D has the following syntax.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Ellipse2D/Java_Ellipse2D_Constructor.htm
---
### Syntax

Ellipse2D() constructor from Ellipse2D has the following syntax.

```java title=Example.java
protected Ellipse2D()
```

### Example

In the following code shows how to use Ellipse2D.Ellipse2D() constructor.

```java title=Example.java
import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;
publicclass Main {
  publicstaticvoid main(String args[]) {
    Ellipse2D.Double e = new Ellipse2D.Double(1.0,2.0,2.0,2.0);
    e.contains(2.0,2.0);
  }
}
```

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
