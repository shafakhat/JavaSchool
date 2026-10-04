---
title: Java Swing Tutorial - Java Font.getFamily()
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Font.getFamily() method.
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Font/0960__Font.getFamily_.htm
---
```java title=Example.java
Back to Font  ↑
```

## Syntax

Font.getFamily() has the following syntax.

```java title=Example.java
public String getFamily()
```

## Example

In the following code shows how to use Font.getFamily() method.

```java title=Example.java
import java.awt.Font;
import java.awt.GraphicsEnvironment;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Font[] fonts  = GraphicsEnvironment.getLocalGraphicsEnvironment().getAllFonts();
    for (int i = 0; i < fonts.length; i++) {
      System.out.print(fonts[i].getFontName() + " : ");
      System.out.print(fonts[i].getFamily() + " : ");
      System.out.print(fonts[i].getName());
      System.out.println();
    }
  }
}
```

The code above generates the following result.

- Back to Font ↑
