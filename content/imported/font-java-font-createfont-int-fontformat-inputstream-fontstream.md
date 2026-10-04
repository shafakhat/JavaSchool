---
title: Java Tutorial - Java Font.createFont(int fontFormat, InputStream fontStream)
nav: Java Tutorial - Java Font....
description: Font.createFont(int fontFormat, InputStream fontStream) has the following syntax.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/Java_Font_createFont_int_fontFormat_InputStream_fontStream_.htm
---
### Syntax

Font.createFont(int fontFormat, InputStream fontStream) has the following syntax.

```java title=Example.java
publicstatic Font createFont(int fontFormat,  InputStream fontStream)   throws FontFormatException ,    IOException
```

### Example

In the following code shows how to use Font.createFont(int fontFormat, InputStream fontStream) method.

```java title=Example.java
import java.awt.Font;
import java.io.FileInputStream;
import java.io.InputStream;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception{
    String fontFileName = "yourfont.ttf";
    InputStream is = new FileInputStream(fontFileName);
    Font ttfBase = Font.createFont(Font.TRUETYPE_FONT, is);
    Font ttfReal = ttfBase.deriveFont(Font.PLAIN, 24);
  }
}
```

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
