---
title: Java Swing Tutorial - Java GraphicsConfiguration .getImageCapabilities ()
nav: Java Swing Tutorial - Java...
description: GraphicsConfiguration.getImageCapabilities() has the following syntax.
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsConfiguration/0300__GraphicsConfiguration.getImageCapabilities_.htm
---
```java title=Example.java
Back to GraphicsConfiguration  ↑
```

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
publicclass Main {
    publicstaticvoid main(String[] argv) {
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice gs = ge.getDefaultScreenDevice();
        GraphicsConfiguration gc = gs.getDefaultConfiguration();
        System.out.println(gc.getImageCapabilities());
    }
}
```

The code above generates the following result.

- Back to GraphicsConfiguration ↑
