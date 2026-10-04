---
title: Override Shape
nav: Override Shape
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20081201073549/http://www.java2s.com:80/Code/Java/Class/OverrideShape.htm
---
Override Shape

```java title=Example.java
// : c10:Shapes.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Shape {
  void draw() {
    System.out.println(this + ".draw()");
  }
}
class Circle extends Shape {
  public String toString() {
    return "Circle";
  }
}
class Square extends Shape {
  public String toString() {
    return "Square";
  }
}
class Triangle extends Shape {
  public String toString() {
    return "Triangle";
  }
}
public class Shapes {
  public static void main(String[] args) {
    // Array of Object, not Shape:
    Object[] shapeList = { new Circle(), new Square(), new Triangle() };
    for (int i = 0; i < shapeList.length; i++)
      ((Shape) shapeList[i]).draw(); // Must cast
  }
} ///:~
```

1.  Polymorphism in Java
---  ---
2.  It only looks like you can override a private or private final method
3.  Method override demo
