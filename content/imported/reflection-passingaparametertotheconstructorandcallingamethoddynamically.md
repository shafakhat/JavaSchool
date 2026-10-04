---
title: Passing a parameter to the constructor and calling a method dynamically
nav: Passing a parameter to the...
description: java.lang.reflect.Constructor constructor = cl.getConstructor(new Class[] { String.class });
section: Imported - java2s Archive
order: 2073
source: https://web.archive.org/web/20140829083919/http://www.java2s.com/Tutorial/Java/0125__Reflection/Passingaparametertotheconstructorandcallingamethoddynamically.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) throws Exception{
      String name = "java.lang.String";
      String methodName = "toLowerCase";
      Class cl = Class.forName(name);
      java.lang.reflect.Constructor constructor = cl.getConstructor(new Class[] { String.class });
      Object invoker = constructor.newInstance(new Object[] { "AAA" });
      Class arguments[] = new Class[] {};
      java.lang.reflect.Method objMethod = cl.getMethod(methodName, arguments);
      Object result = objMethod.invoke(invoker, (Object[]) arguments);
      System.out.println(result);
  }
}
```
