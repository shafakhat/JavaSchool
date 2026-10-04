---
title: Java Swing Tutorial - Java Font.deriveFont(int style, float size)
nav: Java Swing Tutorial - Java...
description: Font.deriveFont(int style, float size) has the following syntax.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/0840__Font.deriveFont_int_style_float_size_.htm
---
## Syntax

Font.deriveFont(int style, float size) has the following syntax.

```java title=Example.java
public Font deriveFont(int style,  float size)
```

## Example

In the following code shows how to use Font.deriveFont(int style, float size) method.

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
