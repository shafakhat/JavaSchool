---
title: Load a Class that is not on the classpath
nav: Load a Class that is not o...
description: Imported from the java2s.com archive: Load a Class that is not on the classpath
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20101106000552/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/LoadaClassthatisnotontheclasspath.htm
---
```java title=Example.java
import java.io.File;
import java.net.URL;
import java.net.URLClassLoader;
public class Main {
  public static void main(String[] argv) throws Exception {
    File file = new File("c:\\class\\");
    URL url = file.toURI().toURL();
    URL[] urls = new URL[] { url };
    ClassLoader loader = new URLClassLoader(urls);
    Class cls = loader.loadClass("user.informatin.Class");
  }
}
```
