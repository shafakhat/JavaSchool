---
title: Static Inner Class
nav: Static Inner Class
description: 1. Nested classes can access all members of all levels of the classes they are nested within
section: Imported - java2s Archive
order: 1074
source: https://web.archive.org/web/20090106043645/http://www.java2s.com:80/Code/Java/Class/StaticInnerClass.htm
---
```java title=Example.java
/**
 * @version 1.00 07 Apr 1998
 * @author Cay Horstmann
 */
public class StaticInnerClassTest {
  public static void main(String[] args) {
    double[] d = new double[20];
    for (int i = 0; i < d.length; i++)
      d[i] = 100 * Math.random();
    ArrayAlg.Pair p = ArrayAlg.minmax(d);
    System.out.println("min = " + p.getFirst());
    System.out.println("max = " + p.getSecond());
  }
}
class ArrayAlg {
  public static class Pair {
    public Pair(double f, double s) {
      first = f;
      second = s;
    }
    public double getFirst() {
      return first;
    }
    public double getSecond() {
      return second;
    }
    private double first;
    private double second;
  }
  public static Pair minmax(double[] d) {
    if (d.length == 0)
      return new Pair(0, 0);
    double min = d[0];
    double max = d[0];
    for (int i = 1; i < d.length; i++) {
      if (min > d[i])
        min = d[i];
      if (max < d[i])
        max = d[i];
    }
    return new Pair(min, max);
  }
}
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
4.  Returning a reference to an inner class
5.  Nesting a class within a scope
6.  Putting test code in a nested class
7.  Inheriting an inner class
8.  Creating a constructor for an anonymous inner class
9.  This file is to show what happens if you try to access an inner class created in another class
10.  Demonstrate an Inner Child class
11.  Demonstrate simple inner class
12.  Just to show that there is no such thing as inner methods in Java
13.  A named inner class is used to
14.  An inner class cannot be overriden like a method
15.  Proper inheritance of an inner class
16.  Using inner classes for callbacks
17.  Holds a sequence of Objects
18.  With concrete or abstract classes, inner classes are the only way to produce the effect
19.  Nested Class Static
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
