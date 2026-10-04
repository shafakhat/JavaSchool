---
title: Getting a Constructor of a Class Object
nav: Getting a Constructor of a...
description: Imported from the java2s.com archive: Getting a Constructor of a Class Object
section: Imported - java2s Archive
order: 2074
source: https://web.archive.org/web/20140829084222/http://www.java2s.com/Tutorial/Java/0125__Reflection/GettingaConstructorofaClassObjectByobtainingalistofallConstructorsobject.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
public class Main {
  public static void main(String[] argv) throws Exception {
    Constructor[] cons = String.class.getDeclaredConstructors();
    for (int i = 0; i < cons.length; i++) {
      Class[] paramTypes = cons[i].getParameterTypes();
      System.out.println(cons[i]);
    }
  }
}
```
