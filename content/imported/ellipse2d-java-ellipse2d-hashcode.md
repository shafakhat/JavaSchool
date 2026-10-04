---
title: Java Tutorial - Java Ellipse2D.hashCode()
nav: Java Tutorial - Java Ellip...
description: In the following code shows how to use Ellipse2D.hashCode() method.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt.geom/Ellipse2D/Java_Ellipse2D_hashCode_.htm
---
### Syntax

Ellipse2D.hashCode() has the following syntax.

```java title=Example.java
public int hashCode()
```

### Example

In the following code shows how to use Ellipse2D.hashCode() method.

```java title=Example.java
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
public class Main {
  public static void main(String args[]) {
    Ellipse2D.Double e = new Ellipse2D.Double(1.0,2.0,2.0,2.0);
    System.out.println(e.hashCode());
  }
}
```

AffineTransformArc2DAreaCubicCurve2DEllipse2DGeneralPath
