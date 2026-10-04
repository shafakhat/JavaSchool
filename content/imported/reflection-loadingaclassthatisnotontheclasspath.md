---
title: Loading a Class That Is Not on the Classpath
nav: Loading a Class That Is No...
description: A URLClassLoader can be used to load classes in any directory.
section: Imported - java2s Archive
order: 2173
source: https://web.archive.org/web/20140829093125/http://www.java2s.com/Tutorial/Java/0125__Reflection/LoadingaClassThatIsNotontheClasspath.htm
---
```java title=Example.java
A URLClassLoader can be used to load classes in any directory.
import java.io.File;
import java.net.URL;
import java.net.URLClassLoader;
public class Main {
  public static void main(String[] argv) throws Exception {
    File file = new File("c:\\");
    URL url = file.toURI().toURL();
    URL[] urls = new URL[] { url };
    ClassLoader cl = new URLClassLoader(urls);
    Class cls = cl.loadClass("com.mycompany.MyClass");
  }
}
```

| 7.11.1. | Loading a Class That Is Not on the Classpath |
|---|---|
| 7.11.2. | Get the path from where a class is loaded |
| 7.11.3. | Obtain from where a Class is loaded |
| 7.11.4. | Load the class source location from Class.getResource() |
| 7.11.5. | Returns a reference to a file with the specified name that is located somewhere on the classpath. |
