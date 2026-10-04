---
title: Method Pointer
nav: Method Pointer
description: printTable(1, 10, 10, MethodPointerTest.class.getMethod("square",
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20081206192244/http://www.java2s.com:80/Code/Java/Class/MethodPointer.htm
---
Method Pointer

```java title=Example.java
/**
 * @version 1.00 11 Mar 1997
 * @author Cay Horstmann
 */
import java.lang.reflect.Method;
import java.text.Format;
public class MethodPointerTest {
  public static void main(String[] args) throws Exception {
    printTable(1, 10, 10, MethodPointerTest.class.getMethod("square",
        new Class[] { double.class }));
    printTable(1, 10, 10, java.lang.Math.class.getMethod("sqrt",
        new Class[] { double.class }));
  }
  public static double square(double x) {
    return x * x;
  }
  public static void printTable(double from, double to, int n, Method f) {
    System.out.println(f);
    double dx = (to - from) / (n - 1);
    for (double x = from; x <= to; x += dx) {
      System.out.println( x);
      try {
        Object[] args = { new Double(x) };
        Double d = (Double) f.invoke(null, args);
        double y = d.doubleValue();
        System.out.println( y);
      } catch (Exception e) {
        System.out.println("???");
      }
    }
  }
}
```

1.  Show a class that has a method and a field with the same name
