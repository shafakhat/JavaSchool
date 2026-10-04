---
title: Java Swing Tutorial - Java Font.deriveFont(float size)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Font.deriveFont(float size) method.
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/0780__Font.deriveFont_float_size_.htm
---
## Syntax

Font.deriveFont(float size) has the following syntax.

```java title=Example.java
public Font deriveFont(float size)
```

## Example

In the following code shows how to use Font.deriveFont(float size) method.

```java title=Example.java
import java.awt.Font;
import java.io.FileInputStream;
import java.io.InputStream;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception{
    String fontFileName = "yourfont.ttf";
    InputStream is = new FileInputStream(fontFileName);
    Font ttfBase = Font.createFont(Font.TRUETYPE_FONT, is);
    Font ttfReal = ttfBase.deriveFont(24F);
  }
}
```
