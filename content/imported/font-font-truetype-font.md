---
title: Java Swing Tutorial - Java Font TRUETYPE_FONT
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Font.TRUETYPE_FONT field.
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/0420__Font.TRUETYPE_FONT.htm
---
## Syntax

Font.TRUETYPE_FONT has the following syntax.

```java title=Example.java
publicstaticfinalint TRUETYPE_FONT
```

## Example

In the following code shows how to use Font.TRUETYPE_FONT field.

```java title=Example.java
import java.awt.Font;
import java.io.InputStream;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
publicclass Main {
  privatestatic String[] names = { "A.ttf" };
  privatestatic Map<String, Font> cache = new ConcurrentHashMap<String, Font>(names.length);
  static {
    for (String name : names) {
      cache.put(name, getFont(name));
    }
  }
  publicstatic Font getFont(String name) {
    Font font = null;
    if (cache != null) {
      if ((font = cache.get(name)) != null) {
        return font;
      }
    }
    String fName = "/fonts/" + name;
    try {
      InputStream is = Main.class.getResourceAsStream(fName);
      font = Font.createFont(Font.TRUETYPE_FONT, is);
    } catch (Exception ex) {
      ex.printStackTrace();
      System.err.println(fName + " not loaded.  Using serif font.");
      font = new Font("serif", Font.PLAIN, 24);
    }
    return font;
  }
}
```
