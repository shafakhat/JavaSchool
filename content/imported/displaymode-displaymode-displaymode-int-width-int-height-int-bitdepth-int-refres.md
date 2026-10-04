---
title: Java Swing Tutorial - Java DisplayMode(int width, int height, int bitDepth, int refreshRate) Constructor
nav: Java Swing Tutorial - Java...
description: DisplayMode(int width, int height, int bitDepth, int refreshRate) constructor from DisplayMode has the following syntax.
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/DisplayMode/0080__DisplayMode.DisplayMode_int_width_int_height_int_bitDepth_int_refreshRate_.htm
---
```java title=Example.java
Back to DisplayMode  ↑
```

## Syntax

DisplayMode(int width, int height, int bitDepth, int refreshRate) constructor from DisplayMode has the following syntax.

```java title=Example.java
public DisplayMode(int width,   int height,   int bitDepth,   int refreshRate)
```

## Example

In the following code shows how to use DisplayMode.DisplayMode(int width, int height, int bitDepth, int refreshRate) constructor.

```java title=Example.java
import java.awt.DisplayMode;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    GraphicsDevice gs = ge.getDefaultScreenDevice();
    boolean canChg = gs.isDisplayChangeSupported();
    if (canChg) {
      DisplayMode displayMode = gs.getDisplayMode();
      int screenWidth = 640;
      int screenHeight = 480;
      int bitDepth = 8;
      displayMode = new DisplayMode(screenWidth, screenHeight, bitDepth, displayMode
          .getRefreshRate());
      try {
        gs.setDisplayMode(displayMode);
      } catch (Throwable e) {
        gs.setFullScreenWindow(null);
      }
    }
  }
}
```

- Back to DisplayMode ↑
