---
title: Getting the Screen Size
nav: Getting the Screen Size
description: Imported from the java2s.com archive: Getting the Screen Size
section: Imported - java2s Archive
order: 1797
source: https://web.archive.org/web/20140829082525/http://www.java2s.com/Tutorial/Java/0120__Development/GettingtheScreenSize.htm
---
```java title=Example.java
import java.awt.Dimension;
import java.awt.Toolkit;
public class Main {
  public static void main(String[] argv) throws Exception {
    Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
    System.out.println(dim);
  }
}
```

| 6.25.1. | java.awt.Toolkit |
|---|---|
| 6.25.2. | Getting the Screen Size |
| 6.25.3. | Centering a Frame, Window, or Dialog on the Screen |
