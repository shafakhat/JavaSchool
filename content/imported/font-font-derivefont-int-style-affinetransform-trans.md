---
title: Java Swing Tutorial - Java Font.deriveFont(int style, AffineTransform trans)
nav: Java Swing Tutorial - Java...
description: Font.deriveFont(int style, AffineTransform trans) has the following syntax.
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/0820__Font.deriveFont_int_style_AffineTransform_trans_.htm
---
## Syntax

Font.deriveFont(int style, AffineTransform trans) has the following syntax.

```java title=Example.java
public Font deriveFont(int style,  AffineTransform trans)
```

## Example

In the following code shows how to use Font.deriveFont(int style, AffineTransform trans) method.

```java title=Example.java
import java.awt.Font;
import java.awt.geom.AffineTransform;
import java.io.FileInputStream;
import java.io.InputStream;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception{
    String fontFileName = "yourfont.ttf";
    InputStream is = new FileInputStream(fontFileName);
    Font ttfBase = Font.createFont(Font.TRUETYPE_FONT, is);
    Font ttfReal = ttfBase.deriveFont(Font.BOLD,AffineTransform.getRotateInstance(0.5));
  }
}
```
