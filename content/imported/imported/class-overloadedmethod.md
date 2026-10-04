---
title: Overloaded method
nav: Overloaded method
description: 1. Demonstration of both constructor and ordinary method overloading
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20090531123156/http://www.java2s.com:80/Code/Java/Class/Overloadedmethod.htm
---
Overloaded method

```java title=Example.java
public class Overloading {
  double method(int i) {
    return i;
  }
  boolean method(boolean b) {
    return !b;
  }
  static double method(int x, double y) {
    return x + y + 1;
  }
  static double method(double x, double y) {
    return x + y + 3;
  }
  public static void main(String[] args) {
    System.out.println(method(10, 20));
    System.out.println(method(10, 20.0));
    System.out.println(method(10.0, 20));
    System.out.println(method(10.0, 20.0));
  }
}
```

1.  Demonstration of both constructor and ordinary method overloading
---  ---
2.  Overloaded constructor
3.  Demonstration of overriding fields
4.  Overloading based on the order of the arguments
5.  Promotion of primitives and overloading
6.  Overloading a base-class method name in a derived class does not hide the base-class versions
7.  Demotion of primitives and overloading
