---
title: Java Swing Tutorial - Java Desktop.browse(URI uri)
nav: Java Swing Tutorial - Java...
description: In the following code shows how to use Desktop.browse(URI uri) method.
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Desktop/0040__Desktop.browse_URI_uri_.htm
---
```java title=Example.java
Back to Desktop  ↑
```

## Syntax

Desktop.browse(URI uri) has the following syntax.

```java title=Example.java
publicvoid browse(URI uri)  throws IOException
```

## Example

In the following code shows how to use Desktop.browse(URI uri) method.

```java title=Example.java
import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
publicclass Main {
  publicstaticvoid main(String[] a) {
    try {
      URI uri = new URI("http:");
      Desktop desktop = null;
      if (Desktop.isDesktopSupported()) {
        desktop = Desktop.getDesktop();
      }
      if (desktop != null)
        desktop.browse(uri);
    } catch (IOException ioe) {
      ioe.printStackTrace();
    } catch (URISyntaxException use) {
      use.printStackTrace();
    }
  }
}
```

- Back to Desktop ↑
