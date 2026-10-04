---
title: Has Declared Constructor
nav: Has Declared Constructor
description: public static boolean hasDeclaredConstructor(Class targetClass, Class[] partypes) {
section: Imported - java2s Archive
order: 2077
source: https://web.archive.org/web/20140829083453/http://www.java2s.com/Tutorial/Java/0125__Reflection/HasDeclaredConstructor.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
public class ReflectionUtils {
  public static boolean hasDeclaredConstructor(Class targetClass, Class[] partypes) {
    Constructor constructor = null;
    try {
      constructor = targetClass.getConstructor(partypes);
    }catch (Exception e) {
      e.printStackTrace();
    }
    return constructor != null;
  }
}
```
