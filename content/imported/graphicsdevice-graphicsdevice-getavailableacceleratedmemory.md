---
title: Java Swing Tutorial - Java GraphicsDevice .getAvailableAcceleratedMemory ()
nav: Java Swing Tutorial - Java...
description: GraphicsDevice.getAvailableAcceleratedMemory() has the following syntax.
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsDevice/0120__GraphicsDevice.getAvailableAcceleratedMemory_.htm
---
## Syntax

GraphicsDevice.getAvailableAcceleratedMemory() has the following syntax.

```java title=Example.java
publicint getAvailableAcceleratedMemory()
```

## Example

In the following code shows how to use GraphicsDevice.getAvailableAcceleratedMemory() method.

```java title=Example.java
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.image.VolatileImage;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    GraphicsDevice[] gs = ge.getScreenDevices();
    for (int i = 0; i < gs.length; i++) {
      VolatileImage im = gs[i].getDefaultConfiguration()
          .createCompatibleVolatileImage(1, 1);
      int bytes = gs[i].getAvailableAcceleratedMemory();
      if (bytes < 0) {
        System.out.println("Amount of memory is unlimited");
      }
      im.flush();
    }
  }
}
```

The code above generates the following result.
