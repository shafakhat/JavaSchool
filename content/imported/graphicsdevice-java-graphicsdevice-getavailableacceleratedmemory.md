---
title: Java GraphicsDevice.getAvailableAcceleratedMemory()
nav: Java GraphicsDevice.getAva...
description: GraphicsDevice getAvailableAcceleratedMemory() this method returns the number of bytes available in accelerated memory on this device. Some images are created or cached i
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsDevice/Java_GraphicsDevice_getAvailableAcceleratedMemory_.htm
---
In this chapter you will learn:

- Get to know GraphicsDevice.getAvailableAcceleratedMemory()
- Syntax for GraphicsDevice.getAvailableAcceleratedMemory()
- Returns for GraphicsDevice.getAvailableAcceleratedMemory()
- Example - GraphicsDevice.getAvailableAcceleratedMemory()

### Description

GraphicsDevice getAvailableAcceleratedMemory() this method returns the number of bytes available in accelerated memory on this device. Some images are created or cached in accelerated memory on a first-come, first-served basis. On some operating systems, this memory is a finite resource.

Calling this method and scheduling the creation and flushing of images carefully may enable applications to make the most efficient use of that finite resource.

Note that the number returned is a snapshot of how much memory is available; some images may still have problems being allocated into that memory.

For example, depending on operating system, driver, memory configuration, and thread situations, the full extent of the size reported may not be available for a given image. There are further inquiry methods on the ImageCapabilities object associated with a VolatileImage that can be used to determine whether a particular VolatileImage has been created in accelerated memory.

### Syntax

GraphicsDevice.getAvailableAcceleratedMemory() has the following syntax.

```java title=Example.java
publicint getAvailableAcceleratedMemory()
```

### Returns

GraphicsDevice.getAvailableAcceleratedMemory() method returns number of bytes available in accelerated memory. A negative return value indicates that the amount of accelerated memory on this GraphicsDevice is indeterminate.

### Example

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

#### Next chapter...

What you will learn in the next chapter:

- Get to know GraphicsDevice.getConfigurations()
- Syntax for GraphicsDevice.getConfigurations()
- Returns for GraphicsDevice.getConfigurations()
- Example - GraphicsDevice.getConfigurations()
