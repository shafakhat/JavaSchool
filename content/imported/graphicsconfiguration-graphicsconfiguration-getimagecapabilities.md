---
title: Java Swing Tutorial - Java GraphicsConfiguration .getImageCapabilities ()
nav: Java Swing Tutorial - Java...
description: GraphicsConfiguration.getImageCapabilities() has the following syntax.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/0300__GraphicsConfiguration.getImageCapabilities_.htm
---
## Syntax

GraphicsConfiguration.getImageCapabilities() has the following syntax.

```java title=Example.java
public ImageCapabilities getImageCapabilities()
```

## Example

In the following code shows how to use GraphicsConfiguration.getImageCapabilities() method.

```java title=Example.java
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
public class Main {
    public static void main(String[] argv) {
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice gs = ge.getDefaultScreenDevice();
        GraphicsConfiguration gc = gs.getDefaultConfiguration();
        System.out.println(gc.getImageCapabilities());
    }
}
```

The code above generates the following result.
