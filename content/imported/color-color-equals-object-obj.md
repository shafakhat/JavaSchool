---
title: Java Swing Tutorial - Java Color.equals(Object obj)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Color.equals(Object obj) method.
section: Imported - java2s Archive
order: 1242
source: https://web.archive.org/web/20150325033240/http://www.java2s.com/Tutorials/Java/java.awt/Color/0780__Color.equals_Object_obj_.htm
---
## Syntax

Color.equals(Object obj) has the following syntax.

```java title=Example.java
public boolean equals(Object obj)
```

## Example

In the following code shows how to use Color.equals(Object obj) method.

```java title=Example.java
import java.awt.Color;
public class Main {
  public static void main(String[] a) {
    Color myBlack = new Color(0, 0, 0); // Color black
    Color myWhite = new Color(255, 255, 255); // Color white
    System.out.println(myBlack.equals(myWhite));
  }
}
```

The code above generates the following result.
