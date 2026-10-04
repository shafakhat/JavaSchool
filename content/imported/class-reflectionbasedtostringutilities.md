---
title: Reflection based toString() utilities
nav: Reflection based toString(...
description: private static void toString(Object o, Class clazz, StringBuilder sb) {
section: Imported - java2s Archive
order: 1063
source: https://web.archive.org/web/20090531211841/http://www.java2s.com:80/Code/Java/Class/ReflectionbasedtoStringutilities.htm
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

1.  ShowToString -- demo program to show default toString methods
---  ---
2.  ToString -- demo program to show a toString method
3.  Demonstrate toString() without an override
4.  To String Demo
5.  Use a generic toString()
