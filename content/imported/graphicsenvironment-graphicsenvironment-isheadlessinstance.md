---
title: Java Swing Tutorial - Java GraphicsEnvironment .isHeadlessInstance ()
nav: Java Swing Tutorial - Java...
description: GraphicsEnvironment.isHeadlessInstance() has the following syntax.
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/GraphicsEnvironment/0260__GraphicsEnvironment.isHeadlessInstance_.htm
---
## Syntax

GraphicsEnvironment.isHeadlessInstance() has the following syntax.

```java title=Example.java
publicboolean isHeadlessInstance()
```

## Example

In the following code shows how to use GraphicsEnvironment.isHeadlessInstance() method.

```java title=Example.java
import java.awt.GraphicsEnvironment;
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println(GraphicsEnvironment.getLocalGraphicsEnvironment()
        .isHeadlessInstance());
  }
}
```

The code above generates the following result.
