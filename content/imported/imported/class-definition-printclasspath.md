---
title: Print classpath
nav: Print classpath
description: ClassLoader sysClassLoader = ClassLoader.getSystemClassLoader();
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20101105235804/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Printclasspath.htm
---
```java title=Example.java
import java.net.URL;
import java.net.URLClassLoader;
public class Main {
  public static void main(String[] args) {
    ClassLoader sysClassLoader = ClassLoader.getSystemClassLoader();
    URL[] urls = ((URLClassLoader) sysClassLoader).getURLs();
    for (int i = 0; i < urls.length; i++) {
      System.out.println(urls[i].getFile());
    }
  }
}
```
