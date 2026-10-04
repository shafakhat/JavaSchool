---
title: Reflection based toString() utilities
nav: Reflection based toString(...
description: private static void toString(Object o, Class clazz, StringBuilder sb) {
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20101106000623/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ReflectionbasedtoStringutilities.htm
---
```java title=Example.java
import java.lang.reflect.Field;
public class Main {
  String hello = "world";
  int i = 42;
  public static void main(String args[]) {
    System.out.println(Util.toString(new MyClass()));
    System.out.println(Util.toString(new MyAnotherClass()));
  }
}
class Util {
  public static String toString(Object o) {
    StringBuilder sb = new StringBuilder();
    toString(o, o.getClass(), sb);
    return o.getClass().getName()+ "\n"+sb.toString();
  }
  private static void toString(Object o, Class clazz, StringBuilder sb) {
    Field f[] = clazz.getDeclaredFields();
    for (int i = 0; i < f.length; i++) {
      f[i].setAccessible(true);
      try {
        sb.append(f[i].getName() + "=" + f[i].get(o)+"\n");
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
    if (clazz.getSuperclass() != null)
      toString(o, clazz.getSuperclass(), sb);
  }
}
class MyClass {
  int i = 1;
  private double d = 3.14;
}
class MyAnotherClass extends MyClass{
  int f = 9;
}
```
