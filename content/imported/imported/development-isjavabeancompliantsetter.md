---
title: Is JavaBean Compliant Setter
nav: Is JavaBean Compliant Setter
description: public static boolean isJavaBeanCompliantSetter (Method method)
section: Imported
order: 20051
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/IsJavaBeanCompliantSetter.htm
---
```java title=Example.java
import java.lang.reflect.Method;
public class Utils {
  public static boolean isJavaBeanCompliantSetter (Method method)
  {
      if (method == null)
          return false;
      if (method.getReturnType() != Void.TYPE)
          return false;
      if (!method.getName().startsWith("set"))
          return false;
      if (method.getParameterTypes().length != 1)
          return false;
      return true;
  }
}
```
