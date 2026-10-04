---
title: Getting a Constructor of a Class Object
nav: Getting a Constructor of a...
description: Constructor con = java.awt.Point.class.getConstructor(new Class[] { int.class, int.class });
section: Imported - java2s Archive
order: 2075
source: https://web.archive.org/web/20140829084324/http://www.java2s.com/Tutorial/Java/0125__Reflection/GettingaConstructorofaClassObjectByobtainingaparticularConstructorobject.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
public class Main {
  public static void main(String[] argv) throws Exception {
    Constructor con = java.awt.Point.class.getConstructor(new Class[] { int.class, int.class });
    System.out.println(con);
  }
}
```
