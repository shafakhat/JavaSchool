---
title: Java Swing Tutorial - Java Color.getColorSpace()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.getColorSpace() method.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/0940__Color.getColorSpace_.htm
---
```java title=Example.java
Back to Color  ↑
```

## Syntax

Color.getColorSpace() has the following syntax.

```java title=Example.java
public ColorSpace getColorSpace()
```

## Example

In the following code shows how to use Color.getColorSpace() method.

```java title=Example.java
import java.awt.Color;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Color myColor = Color.RED;
    System.out.println(myColor.getColorSpace().getNumComponents());
  }
}
```

The code above generates the following result.

- Back to Color ↑
