---
title: Java Swing Tutorial - Java GraphicsEnvironment .preferProportionalFonts ()
nav: Java Swing Tutorial - Java...
description: GraphicsEnvironment.preferProportionalFonts() has the following syntax.
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsEnvironment/0300__GraphicsEnvironment.preferProportionalFonts_.htm
---
## Syntax

GraphicsEnvironment.preferProportionalFonts() has the following syntax.

```java title=Example.java
public void preferProportionalFonts()
```

## Example

In the following code shows how to use GraphicsEnvironment.preferProportionalFonts() method.

```java title=Example.java
import java.awt.GraphicsEnvironment;
public class Main {
  public static void main(String[] args) {
    GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
    ge.preferProportionalFonts();
  }
}
```
