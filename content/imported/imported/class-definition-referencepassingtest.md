---
title: Reference Passing Test
nav: Reference Passing Test
description: Imported from the java2s.com archive: Reference Passing Test
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20070328231612/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ReferencePassingTest.htm
---
```java title=Example.java
class Point {
  public int x;
  public int y;
}
public class MainClass {
  public static void increment(int x) {
    x++;
  }
  public static void reset(Point point) {
    point.x = 0;
    point.y = 0;
  }
  public static void main(String[] args) {
    int a = 9;
    increment(a);
    System.out.println(a); // prints 9
    Point p = new Point();
    p.x = 400;
    p.y = 600;
    reset(p);
    System.out.println(p.x); // prints 0
  }
}
```

```java title=Example.java

9
0
```
