---
title: Root list with File.listRoots()
nav: Root list with File.listRo...
description: Imported from the java2s.com archive: Root list with File.listRoots()
section: Imported - java2s Archive
order: 1880
source: https://web.archive.org/web/20140829081044/http://www.java2s.com/Tutorial/Java/0120__Development/RootlistwithFilelistRoots.htm
---
```java title=Example.java
import java.io.File;
public class MainClass {
  public static void main(String[] args) {
    File[] roots = File.listRoots();
    for (int i = 0; i < roots.length; i++) {
      System.out.println(roots[i]);
    }
  }
}
```

| 6.38.1. | Home Directory |
|---|---|
| 6.38.2. | Default Directory |
| 6.38.3. | The roots of this filesystem |
| 6.38.4. | Root list with File.listRoots() |
