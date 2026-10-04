---
title: Overloaded constructor
nav: Overloaded constructor
description: 1. Demonstration of both constructor and ordinary method overloading
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20090530094200/http://www.java2s.com:80/Code/Java/Class/Overloadedconstructor.htm
---
```java title=Example.java
public class Point {
  int x, y;
  Point(int x, int y) // Overloaded constructor
  {
    this.x = x;
    this.y = y;
  }
  Point(Point p) // Overloaded constructor
  {
    this(p.x, p.y);
  } // Calls the first constructor
  void move(int dx, int dy) {
    x += dx;
    y += dy;
  }
  public String toString() {
    return "(" + x + ", " + y + ")";
  }
}
```

1.  Demonstration of both constructor and ordinary method overloading
---  ---
2.  Overloaded method
3.  Demonstration of overriding fields
4.  Overloading based on the order of the arguments
5.  Promotion of primitives and overloading
6.  Overloading a base-class method name in a derived class does not hide the base-class versions
7.  Demotion of primitives and overloading
