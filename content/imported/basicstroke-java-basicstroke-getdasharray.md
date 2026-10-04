---
title: Java BasicStroke.getDashArray()
nav: Java BasicStroke.getDashAr...
description: BasicStroke getDashArray() returns the array representing the lengths of the dash segments. Alternate entries in the array represent the user space lengths of the opaque
section: Imported - java2s Archive
order: 1151
source: https://web.archive.org/web/20140418094627/http://www.java2s.com/Tutorials/Java/java.awt/BasicStroke/Java_BasicStroke_getDashArray_.htm
---
In this chapter you will learn:

- Get to know BasicStroke.getDashArray()
- Syntax for BasicStroke.getDashArray()
- Returns for BasicStroke.getDashArray()
- Example - BasicStroke.getDashArray()

### Description

BasicStroke getDashArray() returns the array representing the lengths of the dash segments. Alternate entries in the array represent the user space lengths of the opaque and transparent segments of the dashes. As the pen moves along the outline of the Shape to be stroked, the user space distance that the pen travels is accumulated. The distance value is used to index into the dash array. The pen is opaque when its current cumulative distance maps to an even element of the dash array and transparent otherwise.

### Syntax

BasicStroke.getDashArray() has the following syntax.

```java title=Example.java
public float[] getDashArray()
```

### Returns

BasicStroke.getDashArray() method returns the dash array.

### Example

In the following code shows how to use BasicStroke.getDashArray() method.

```java title=Example.java
import java.awt.BasicStroke;
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    BasicStroke stroke = new BasicStroke(10, BasicStroke.CAP_BUTT, BasicStroke.JOIN_BEVEL, 0.1F);
    System.out.println(Arrays.toString(stroke.getDashArray()));
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Get to know BasicStroke.getDashPhase()
- Syntax for BasicStroke.getDashPhase()
- Returns for BasicStroke.getDashPhase()
- Example - BasicStroke.getDashPhase()
