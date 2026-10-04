---
title: Polymorphism in Java
nav: Polymorphism in Java
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1059
source: https://web.archive.org/web/20081201082155/http://www.java2s.com:80/Code/Java/Class/PolymorphisminJava.htm
---
Polymorphism in Java

```java title=Example.java
// : c07:Shapes.java
// Polymorphism in Java.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.Random;
class Shape {
  void draw() {
  }
  void erase() {
  }
}
class Circle extends Shape {
  void draw() {
    System.out.println("Circle.draw()");
  }
  void erase() {
    System.out.println("Circle.erase()");
  }
}
class Square extends Shape {
  void draw() {
    System.out.println("Square.draw()");
  }
  void erase() {
    System.out.println("Square.erase()");
  }
}
class Triangle extends Shape {
  void draw() {
    System.out.println("Triangle.draw()");
  }
  void erase() {
    System.out.println("Triangle.erase()");
  }
}
// A "factory" that randomly creates shapes:
class RandomShapeGenerator {
  private Random rand = new Random();
  public Shape next() {
    switch (rand.nextInt(3)) {
    default:
    case 0:
      return new Circle();
    case 1:
      return new Square();
    case 2:
      return new Triangle();
    }
  }
}
public class ShapesDemo {
  private static RandomShapeGenerator gen = new RandomShapeGenerator();
  public static void main(String[] args) {
    Shape[] s = new Shape[9];
    // Fill up the array with shapes:
    for (int i = 0; i < s.length; i++)
      s[i] = gen.next();
    // Make polymorphic method calls:
    for (int i = 0; i < s.length; i++)
      s[i].draw();
  }
} ///:~
```

1.  It only looks like you can override a private or private final method
---  ---
2.  Override Shape
3.  Method override demo
