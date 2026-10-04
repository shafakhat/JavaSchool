---
title: Java Swing Tutorial - Java Color.getColorSpace()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.getColorSpace() method.
section: Imported - java2s Archive
order: 1233
source: https://web.archive.org/web/20150325030721/http://www.java2s.com/Tutorials/Java/java.awt/Color/0940__Color.getColorSpace_.htm
---
## Syntax

Color.getColorSpace() has the following syntax.

```java title=Example.java
public ColorSpace getColorSpace()
```

## Example

In the following code shows how to use Color.getColorSpace() method.

```java title=Example.java
import java.awt.Color;
public class Main {
  public static void main(String[] args) {
    Color myColor = Color.RED;
    System.out.println(myColor.getColorSpace().getNumComponents());
  }
}
```

The code above generates the following result.
